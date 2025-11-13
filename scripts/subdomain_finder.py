#!/usr/bin/env python3
"""
Subdomain Enumeration Tool
Procura subdomínios comuns de um alvo
"""

import requests
import sys

def check_subdomain(subdomain, domain):
    """Verifica se subdomain existe"""
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=2)
        return True
    except:
        return False

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <domain.com>")
        sys.exit(1)
    
    domain = sys.argv[1]
    
    # Lista de subdomínios comuns
    subdomains = [
        'www', 'mail', 'ftp', 'admin', 'blog', 'shop',
        'dev', 'test', 'staging', 'api', 'portal',
        'secure', 'vpn', 'remote', 'cloud', 'mobile',
        'webmail', 'support', 'help', 'login', 'dashboard'
    ]
    
    print(f"\n🔍 A procurar subdomínios de {domain}...\n")
    found = []
    
    for sub in subdomains:
        full_domain = f"{sub}.{domain}"
        if check_subdomain(sub, domain):
            print(f"✅ Encontrado: {full_domain}")
            found.append(full_domain)
        else:
            print(f"❌ Não existe: {full_domain}", end='\r')
    
    print(f"\n\n📊 Total encontrados: {len(found)}")
    
    # Guarda resultados
    if found:
        with open(f"subdomains_{domain}.txt", 'w') as f:
            for subdomain in found:
                f.write(f"{subdomain}\n")
        print(f"💾 Resultados guardados em: subdomains_{domain}.txt")

if __name__ == "__main__":
    main()
