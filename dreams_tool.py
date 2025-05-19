import os
import sys
import time
from colorama import Fore, Style, init
import socket
import requests

init(autoreset=True)

# Centering function
def center(text, width=100):
    return text.center(width)

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
from colorama import Fore, Style
import pyfiglet

def center(text, width=100):
    return text.center(width)

# Großes DREAM mit pyfiglet
dream_big = pyfiglet.figlet_format("DREAM")

header = f"""
{Fore.RED}{Style.BRIGHT}
{'='*100}
{center(dream_big)}
{center('MultiTool By Dream Discord:zy.dream')}
{'='*100}
{Style.RESET_ALL}
"""

print(header)

# Tools List (Flat with numbering)
tools = [
    "IP Lookup", "Whois Lookup", "DNS Lookup", "Email Breach Check",
    "Subdomain Scanner", "HTTP Headers Grabber", "Port Scanner", "Geo Locator",
    "Banner Grabber", "Ping Sweeper", "Traceroute", "SQLi Tester",
    "XSS Tester", "Reverse Shell Generator", "Payload Generator",
    "Command Injection Test", "SSH Brute Force", "FTP Brute Force",
    "Form Brute Force", "Hash Cracker", "Hash Generator", "File Encryptor",
    "File Decryptor", "Base64 Encoder/Decoder", "Packet Sniffer",
    "MAC Address Changer", "VPN Detection", "ARP Spoofer", "Wi-Fi Scanner",
    "Phishing Email Generator", "Fake Login Page", "Clipboard Logger"
]

# IP Lookup Example Function
def ip_lookup():
    ip = input("\nEnter IP address or hostname: ")
    try:
        ip_info = socket.gethostbyname(ip)
        print(f"\n{Fore.RED}Resolved IP: {ip_info}\n")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}\n")
    input("Press Enter to return to the menu...")

# Tool functions mapping
functions = {
    1: ip_lookup
    # Add more real functions here
}

# Print Menu
def print_menu():
    clear()
    print(header)
    print(Fore.RED + Style.BRIGHT + center("Main Menu - Over 30 Tools Available"))
    print(Fore.RED + Style.BRIGHT + "="*100)

    for i in range(0, len(tools), 3):
        row = tools[i:i+3]
        line = "   ".join([f"[{i+j+1:2}] {tool:<24}" for j, tool in enumerate(row)])
        print(center(line))

    print("\n" + Fore.RED + Style.BRIGHT + "="*100 + "\n")
    print(center("Enter the number of the tool to run it."))
    print(center("Type Q to quit."))

# Main Loop
print_menu()
try:
    while True:
        choice = input(Fore.RED + Style.BRIGHT + "Your choice (Q to quit): ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(tools):
            tool_number = int(choice)
            if tool_number in functions:
                functions[tool_number]()
            else:
                print(f"\n{Fore.RED}[!] Tool '{tools[tool_number-1]}' is not implemented yet.\n")
                input("Press Enter to return to menu...")
            print_menu()
        else:
            print(Fore.RED + "[!] Invalid choice. Try again.")
except KeyboardInterrupt:
    print("\nExiting...")

