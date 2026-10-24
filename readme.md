# Guard-X Local Pro 🛡️

A robust, local anti-theft and Bluetooth device monitoring system built with **FastAPI** and native **Windows PowerShell** commands (`Get-PnpDevice`). It eliminates complex or incompatible Python Bluetooth libraries, providing a direct, reliable, and real-time tracking mechanism for your devices.

## ✨ Key Features

* **Pure Windows Integration:** Leverages native PowerShell commands (`Get-PnpDevice`) to accurately query connected Bluetooth and audio endpoint devices without external dependency conflicts.

* **Real-Time Live Monitoring:** Automatically checks device status every 5 seconds with a built-in live countdown timer.

* **Emergency Siren Alarm:** Triggers an immediate browser-based Web Audio API siren alert if any protected device disconnects or disappears from Windows.

* **Lightweight & Fast:** Built on top of FastAPI and Tailwind CSS for a modern, responsive, and slick user interface.

* **Local Privacy-First Design:** Operates entirely on your local Windows machine, ensuring complete privacy and direct hardware communication.

## 📂 Project Structure

```
ble_tracker_app/
│
├── main.py              # FastAPI main application and routing
├── ble_service.py       # Windows PowerShell Bluetooth scanner service
└── templates/
    └── index.html       # Interactive responsive UI with real-time tracking & siren

```

## 🚀 Installation & Running Locally

### Prerequisites

* Python 3.8 or higher installed on a **Windows** machine.

### Steps

1. **Clone or Download the repository:**

   ```
   git clone https://github.com/Boss-311/guard-x-protection.git
   cd guard-x-protection
   
   ```

2. **Install Dependencies:**

   ```
   pip install fastapi uvicorn
   
   ```

3. **Run the Application:**

   ```
   python main.py
   
   ```

4. **Open in Browser:**
   Open your Google Chrome browser and navigate to:

   ```
   http://127.0.0.1:8000
   
   ```

## 🛠️ How to Use

1. Click on **"تحديث القائمة من ويندوز"** to fetch your currently connected Bluetooth and audio devices from Windows.

2. Click **"➕ اختيار"** on any device to add it to your Protected Devices list.

3. Click **"🚀 تشغيل المراقبة الحية"** to activate the automated 5-second health check loop.

4. If a protected device disconnects, the system will instantly flag it as missing and sound the emergency siren!

## 📜 License

Developed for personal local security and advanced hardware monitoring.