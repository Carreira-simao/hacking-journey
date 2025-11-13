#!/usr/bin/env python3
"""
Port Scanner Avançado
Com threading para ser mais rápido!
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def scan_port(host, port):
    """Tenta conectar a uma porta"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            # Tenta identificar o serviço
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            return (port, service)
    except:
        pass
    return None

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <host>")
        sys.exit(1)
    
    host = sys.argv[1]
    
    print(f"""
    ╔══════════════════════════════════════╗
    ║   🔍 PORT SCANNER AVANÇADO 🔍       ║
    ╚══════════════════════════════════════╝
    
    🎯 Alvo: {host}
    ⏰ Início: {datetime.now().strftime('%H:%M:%S')}
    
    """)
    
    # Portas mais comuns (top 20)
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 111, 135, 139,
        143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080
    ]
    
    open_ports = []
    
    print("🔌 A escanear portas...\n")
    
    # Usa threading para ser mais rápido
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda p: scan_port(host, p), common_ports)
        
        for result in results:
            if result:
                port, service = result
                print(f"✅ Porta {port:5d} ABERTA - Serviço: {service}")
                open_ports.append((port, service))
    
    print(f"""
    
    ╔══════════════════════════════════════╗
    ║          📊 RESULTADOS              ║
    ╚══════════════════════════════════════╝
    
    Portas abertas: {len(open_ports)}
    ⏰ Fim: {datetime.now().strftime('%H:%M:%S')}
    
    """)
    
    # Guarda resultados
    if open_ports:
        filename = f"scan_{host}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Scan de {host}\n")
            f.write(f"Data: {datetime.now()}\n\n")
            for port, service in open_ports:
                f.write(f"Porta {port} - {service}\n")
        print(f"💾 Resultados guardados: {filename}")

if __name__ == "__main__":
    main()
