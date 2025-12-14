#!/usr/bin/env python3
import os
import sys
import time
import socket
import requests

def clear():
    os.system('clear')

def banner():
    clear()
    print("""
    ╔════════════════════════════╗
    ║       🐉 FRON v2.0 🐉      ║
    ║    FuriaDaNoitePlay        ║
    ╚════════════════════════════╝
    """)

def menu():
    print("""
    [1] Scanner de Rede
    [2] Teste de Ping
    [3] Ver Meu IP
    [4] Teste de Conexão
    [5] Informações do Sistema
    [6] Sair
    """)
    return input("👉 Escolha uma opção: ")

def scanner_rede():
    print("\n[+] Scanner de Rede...")
    os.system('ifconfig')
    input("\nPressione Enter para continuar...")

def teste_ping():
    site = input("\n[?] Site para ping (ex: google.com): ")
    print(f"\n[+] Pingando {site}...")
    os.system(f'ping -c 4 {site}')
    input("\nPressione Enter para continuar...")

def meu_ip():
    print("\n[+] Obtendo IP...")
    try:
        ip = requests.get('https://api.ipify.org').text
        print(f"✅ Seu IP público: {ip}")
    except:
        print("❌ Erro ao obter IP")
    input("\nPressione Enter para continuar...")

def teste_conexao():
    print("\n[+] Testando conexão...")
    sites = ['google.com', 'github.com', 'youtube.com']
    for site in sites:
        print(f"\nTestando {site}...")
        os.system(f'ping -c 1 {site} > /dev/null && echo "✅ Online" || echo "❌ Offline"')
    input("\nPressione Enter para continuar...")

def info_sistema():
    print("\n[+] Informações do Sistema:")
    os.system('uname -a')
    print("\n[+] Memória:")
    os.system('free -h')
    print("\n[+] Armazenamento:")
    os.system('df -h')
    input("\nPressione Enter para continuar...")

def main():
    while True:
        banner()
        opcao = menu()
        
        if opcao == '1':
            scanner_rede()
        elif opcao == '2':
            teste_ping()
        elif opcao == '3':
            meu_ip()
        elif opcao == '4':
            teste_conexao()
        elif opcao == '5':
            info_sistema()
        elif opcao == '6':
            print("\n👋 Saindo do FRON...")
            time.sleep(1)
            break
        else:
            print("\n❌ Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Programa interrompido!")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
