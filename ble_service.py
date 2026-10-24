import subprocess
import platform
import json
import logging

logging.basicConfig(level=logging.INFO)

class MultiBluetoothTracker:
    def __init__(self):
        pass

    async def scan_near_devices(self):
        print("🔍 جاري جلب أجهزة البلوتوث المتصلة من ويندوز...")
        devices_list = []
        if platform.system() == "Windows":
            # سكريبت PowerShell لسحب الأجهزة المتصلة وحالتها من ويندوز
            cmd = 'powershell -Command "Get-PnpDevice -Status OK -ErrorAction SilentlyContinue | Where-Object {$_.Class -eq \'Bluetooth\' -or $_.Class -eq \'AudioEndpoint\'} | Select-Object FriendlyName, InstanceId, Status | ConvertTo-Json"'
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=5)
                if result.returncode == 0 and result.stdout.strip():
                    data = json.loads(result.stdout)
                    if isinstance(data, dict):
                        data = [data]
                    seen = set()
                    for item in data:
                        name = item.get("FriendlyName")
                        inst_id = item.get("InstanceId")
                        status = item.get("Status")
                        if name and inst_id and name not in seen:
                            seen.add(name)
                            devices_list.append({
                                "name": name,
                                "address": inst_id,
                                "rssi": f"الحالة: {status}" if status else "متصل بنجاح"
                            })
            except Exception as e:
                print(f"Scan error: {e}")
        return devices_list