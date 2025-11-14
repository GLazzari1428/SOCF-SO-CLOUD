from flask import Flask, jsonify
import os
import platform
import psutil

APP = Flask(__name__)

INTEGRANTES = "Gustavo Tasca Lazzari" 

def get_system_info():
    process = psutil.Process(os.getpid())
    
    memory_info = process.memory_info()
    memory_mb = memory_info.rss / (1024 * 1024)
    
    cpu_percent = process.cpu_percent(interval=0.1)
    
    os_name = platform.system()
    os_version = platform.release()
    
    return {
        "nome": INTEGRANTES,
        "pid": os.getpid(),
        "memoria_usada_mb": round(memory_mb, 2),
        "cpu_percent": round(cpu_percent, 2),
        "sistema_operacional": f"{os_name} ({os_version})"
    }

@APP.route('/')
def home():
    info = get_system_info()
    
    html = f"""
    <html>
    <head><title>System Information</title></head>
    <body>
        <h1>Informações do Sistema</h1>
        <p><strong>Nome:</strong> {info['nome']}</p>
        <p><strong>PID:</strong> {info['pid']}</p>
        <p><strong>Memória usada:</strong> {info['memoria_usada_mb']} MB</p>
        <p><strong>CPU:</strong> {info['cpu_percent']}%</p>
        <p><strong>Sistema Operacional:</strong> {info['sistema_operacional']}</p>
    </body>
    </html>
    """
    return html

@APP.route('/info')
def info():
    return jsonify({
        "integrantes": INTEGRANTES
    })

@APP.route('/metricas')
def metricas():
    return jsonify(get_system_info())

if __name__ == '__app__':
    APP.run(debug=True, host='0.0.0.0', port=5000)