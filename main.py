from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from ble_service import MultiBluetoothTracker

app = FastAPI(title="Guard-X Direct Anti-Theft")
tracker = MultiBluetoothTracker()

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    if os.path.exists("templates/index.html"):
        with open("templates/index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>ملف templates/index.html غير موجود!</h1>"

@app.get("/api/scan")
async def scan_devices():
    devices = await tracker.scan_near_devices()
    return {"status": "success", "devices": devices}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)