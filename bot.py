import requests
import random
import time
import os
from colorama import Fore, init


init(autoreset=True)


banner = """
██████╗░██╗░░░██╗███████╗░█████╗░███╗░░░███╗██╗░░██╗
██╔══██╗██║░░░██║██╔════╝██╔══██╗████╗░████║╚██╗██╔╝
██████╔╝██║░░░██║█████╗░░██║░░██║██╔████╔██║░╚███╔╝░
██╔═══╝░██║░░░██║██╔══╝░░██║░░██║██║╚██╔╝██║░██╔██╗░
██║░░░░░╚██████╔╝███████╗╚█████╔╝██║░╚═╝░██║██╔╝╚██╗
╚═╝░░░░░░╚═════╝░╚══════╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝
=========================================================================
Author: HarunTampan
Script: Auto Text Discord
=========================================================================
PERINGATAN : RESIKO DI TANGGUNG MASING-MASING KALAU DI BANNED DI DC
=========================================================================
"""


print(banner)


channel_id = input("Masukkan ID channel: ").strip()
waktu1 = int(input("Set Waktu Hapus Pesan (detik): "))
waktu2 = int(input("Set Waktu Kirim Pesan (detik): "))


for i in range(3, 0, -1):
    print(i)
    time.sleep(1)


os.system('cls' if os.name == 'nt' else 'clear')


with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()


while True:
    
    payload = {'content': random.choice(words).strip()}
    headers = {'Authorization': authorization}


    
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    if response.status_code == 200:
        print(Fore.WHITE + "Sent message: " + Fore.YELLOW + payload['content'])
    else:
        print(Fore.RED + f"Failed to send message: {response.status_code}")
        break

    
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    if response.status_code == 200:
        messages = response.json()
        if not messages:
            print(Fore.RED + "No messages found in the channel.")
            break

        time.sleep(waktu1)

        
        message_id = messages[0]['id']
        response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
        if response.status_code == 204:
            print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
        else:
            print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')
    else:
        print(Fore.RED + f'Gagal mendapatkan pesan di channel: {response.status_code}')
        break

    time.sleep(waktu2)
