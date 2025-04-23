from flask import Flask, render_template
import psutil
import os

app = Flask(__name__)

def get_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_raw = f.read()
            temp_c = float(temp_raw) / 1000.0
            return f"{temp_c:.1f}°C"
    except:
        return "Unavailable"

@app.route('/')
def dashboard():
    cpu_temp = get_temp()
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return render_template("index.html",
        cpu_temp=cpu_temp,
        cpu_percent=cpu_percent,
        ram_percent=ram.percent,
        disk_percent=disk.percent
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
