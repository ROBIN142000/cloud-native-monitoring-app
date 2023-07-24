import psutil as monitor
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cpuPer = monitor.cpu_percent()
    memUti = monitor.virtual_memory().percent
    Message = None

    if cpuPer > 80:
            Message = 'CPU usage more than 80 percent, you need to scale up'
    elif memUti > 80:
            Message = 'Memory usage more than 80 percent, you need to scale up'

    return render_template("index.html", cpu_metric=cpuPer, mem_metric=memUti, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
