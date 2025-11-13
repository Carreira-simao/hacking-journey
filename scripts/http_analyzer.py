#!/usr/bin/env python3
"""
HTTP Header Analyzer
Analisa headers de segurança de websites
"""

import requests
import sys

def analyze_headers(url):
    """Analisa headers HTTP"""
    
    if not url.startswith('http'):
        url = f"http://{url}"
    
    print(f"\n🌐 A analisar: {url}\n")
    
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"🔗 URL Final: {response.url}\n")
        
        # Headers importantes de segurança
        security_headers = {
            'Strict-Transport-Security': 'HSTS',
            'X-Frame-Options': 'Clickjacking Protection',
            'X-Content-Type-Options': 'MIME Sniffing Protection',
            'Content-Security-Policy': 'CSP',
            'X-XSS-Protection': 'XSS Protection',
            'Referrer-Policy': 'Referrer Policy'
        }
        
        print("🔒 HEADERS DE SEGURANÇA:")
        print("=" * 50)
        
        for header, description in security_headers.items():
            if header in response.headers:
                print(f"✅ {description:30s} | {header}")
                print(f"   Valor: {response.headers[header]}\n")
            else:
                print(f"❌ {description:30s} | AUSENTE\n")
        
        print("\n📋 TODOS OS HEADERS:")
        print("=" * 50)
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        
        # Guarda resultados
        filename = f"headers_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Análise de Headers: {url}\n")
            f.write("=" * 50 + "\n\n")
            for header, value in response.headers.items():
                f.write(f"{header}: {value}\n")
        
        print(f"\n💾 Análise guardada: {filename}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    analyze_headers(url)

if __name__ == "__main__":
    main()
