import streamlit as st
import pandas as pd
import plotly.express as px
from scapy.all import sniff, IP, TCP, UDP, ARP
import threading
import time
from collections import deque

# --- CONFIGURATION ---
st.set_page_config(page_title="Network Traffic Analyzer", layout="wide", page_icon="🛡️")

# --- SHARED MEMORY (The Fix) ---
# We use @st.cache_resource to ensure this list is created ONLY ONCE
# and is shared between the background thread and the dashboard.
@st.cache_resource
def get_shared_buffer():
    return deque(maxlen=1000)

@st.cache_resource
def get_sniffer_status():
    return {"running": False}

shared_buffer = get_shared_buffer()
sniffer_status = get_sniffer_status()

# --- SESSION STATE ---
if 'display_data' not in st.session_state:
    st.session_state.display_data = deque(maxlen=1000)

# --- BACKEND: PACKET SNIFFER ---
def process_packet(packet):
    try:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            proto_num = packet[IP].proto
            
            protocol = "Other"
            if proto_num == 6: protocol = "TCP"
            elif proto_num == 17: protocol = "UDP"
            elif proto_num == 1: protocol = "ICMP"

            packet_info = {
                "Time": time.strftime("%H:%M:%S"),
                "Source": src_ip,
                "Destination": dst_ip,
                "Protocol": protocol,
                "Length": len(packet)
            }
            # Write to the PERMANENT shared buffer
            shared_buffer.append(packet_info)
    except Exception:
        pass

def start_sniffing():
    # Remove 'iface' argument to let Scapy auto-detect the best interface
    sniff(prn=process_packet, store=False, iface="en0")

# --- FRONTEND: DASHBOARD ---
st.title("🛡️ Network Traffic Analyzer")

# Controls
col1, col2 = st.columns([1, 8])
with col1:
    if st.button('Start Sniffing'):
        if not sniffer_status["running"]:
            sniffer_status["running"] = True
            t = threading.Thread(target=start_sniffing, daemon=True)
            t.start()
            st.rerun()

# Data Sync (Move from Buffer to Display)
# We transfer items so the buffer clears out and doesn't re-add old packets
while shared_buffer:
    st.session_state.display_data.append(shared_buffer.popleft())

# Status & Auto-Refresh
if sniffer_status["running"]:
    st.success(f"🟢 Sniffer Running... Captured {len(st.session_state.display_data)} packets")
    time.sleep(1) 
    st.rerun() # Keep refreshing to pull new data
else:
    st.warning("🔴 Sniffer Stopped")

# --- VISUALIZATION ---
if len(st.session_state.display_data) > 0:
    df = pd.DataFrame(st.session_state.display_data)

    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Packets", len(df))
    m2.metric("Unique IPs", df['Source'].nunique())
    m3.metric("Top Protocol", df['Protocol'].mode()[0])

    # Charts
    c1, c2 = st.columns(2)
    with c1:
        fig_proto = px.pie(df, names='Protocol', title='Protocol Distribution')
        st.plotly_chart(fig_proto, use_container_width=True)
    with c2:
        src_counts = df['Source'].value_counts().head(5).reset_index()
        src_counts.columns = ['IP', 'Count']
        fig_src = px.bar(src_counts, x='IP', y='Count', title='Top Sources')
        st.plotly_chart(fig_src, use_container_width=True)

    # Data Table
    st.subheader("Live Packet Feed")
    st.dataframe(df.tail(10), use_container_width=True)
else:
    st.info("Waiting for traffic... (Run 'ping google.com' in terminal)")