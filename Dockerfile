FROM python:3.9-slim

# Install system dependencies required for Scapy
RUN apt-get update && apt-get install -y \
    libpcap-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port Streamlit runs on
EXPOSE 8080

# Run Streamlit
CMD ["streamlit", "run", "net_analyzer.py", "--server.port=8080", "--server.address=0.0.0.0"]
