import requests

API_KEY = "YOUR_API_KEY"

ip_address = input("Enter IP address: ")

url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip_address}/general"

headers = {
    "X-OTX-API-KEY": API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    pulse_count = data.get("pulse_info", {}).get("count", 0)

    print("\n[+] Threat Intelligence Result\n")
    print(f"IOC: {ip_address}")
    print(f"Pulse Count: {pulse_count}")

    if pulse_count > 0:
        print("Reputation: Suspicious / Malicious")
    else:
        print("Reputation: Clean")

else:
    print("[ERROR] Failed to fetch threat intelligence.")
