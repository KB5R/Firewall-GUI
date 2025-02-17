
#import nftables
#import json

#nft = nftables.Nftables()
#nft.set_json_output(True)
#rc, output, error = nft.cmd("list ruleset")
#print(json.loads(output))

#----------------
# After brainstorming I decided to change the approach
# После мозгового штурма решил изменить подход
#----------------


#! /usr/bin/python3


import os
import subprocess
from datetime import datetime



# Функция по отключению fi
def run_remove_firewall():
    try:
        subprocess.run(["bash", "remove_firewall.sh"], check=True)
        print("Скрипт remove_firewall.sh успешно выполнен.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении remove_firewall.sh: {e}")

# run_remove_firewall()






def clear_firewall():
    confirm = input('Подтвердите вы уверены что хотите очистить firewall (Y/N) ')
    if confirm.lower() == 'y':
        try:
            # nft flush ruleset
            subprocess.run(["nft", "flush", "ruleset"], check=True)
            print("Правила успешно очищены.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении команды: {e}")





def main():
    print("\nМеню:")
    print("1. Очистить  firewall (nftables)")
    print("2. Важно для стабильной работы nftables! Удаление сторонних firewall (iptables, firewalld)")
    print("3. Выйти")

main()

number = int(input('Сделайте выбор сценария: '))
if number == 1:
    run_remove_firewall()
elif number == 2:
    clear_firewall()
else:
    print('Некорректный выбор, попробуйте ещё раз.')
