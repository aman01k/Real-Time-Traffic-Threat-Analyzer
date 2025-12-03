# 🛡️ Real-Time Traffic Threat Analyzer

A powerful, real-time network traffic analysis dashboard built with **Python** and **Streamlit**. This tool captures network packets, analyzes protocols, and visualizes traffic patterns in an interactive dashboard.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

## ✨ Features

- **🕵️ Real-Time Packet Sniffing**: Captures TCP, UDP, and ICMP packets using `Scapy`.
- **📊 Interactive Visualizations**:
    - Protocol Distribution (Pie Chart)
    - Top Source IPs (Bar Chart)
    - Live Packet Feed (Data Table)
- **🧪 Traffic Simulation Mode**: Generate synthetic traffic data for demonstrations or when running in isolated environments (like Cloud Run).
- **🐳 Dockerized**: Fully containerized for easy deployment.
- **☁️ Cloud Ready**: Includes scripts for one-click deployment to Google Cloud Run.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional, for containerization)
- Google Cloud SDK (optional, for deployment)

### 💻 Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aman01k/Real-Time-Traffic-Threat-Analyzer.git
   cd Real-Time-Traffic-Threat-Analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run net_analyzer.py
   ```
   *Note: You may need `sudo` privileges for packet sniffing on some systems.*

### 🐳 Running with Docker

We provide a helper script to build and run the container locally:

```bash
./local_run.sh
```
Access the dashboard at `http://localhost:8080`.

## ☁️ Deployment

### Google Cloud Run

Deploying to Google Cloud Run is automated with the included script.

1. **Authenticate with Google Cloud**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

2. **Deploy**
   ```bash
   ./deploy.sh
   ```

This will build the image using Cloud Build and deploy it to a public Cloud Run service.

> **Note on Cloud Deployment**: Cloud Run containers are isolated. To see the dashboard in action on the cloud, use the **"Simulate Traffic"** checkbox in the app to generate demo data.

## 🛠️ Built With

- **[Streamlit](https://streamlit.io/)** - The web framework used.
- **[Scapy](https://scapy.net/)** - Packet manipulation and sniffing.
- **[Plotly](https://plotly.com/)** - Interactive graphing library.
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation.

## 📄 License

This project is licensed under the MIT License.
