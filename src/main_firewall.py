
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

# Remove iptables and firewalld
def run_remove_firewall():
    try:
        subprocess.run(["bash", "./programs/remove_firewall.sh"], check=True)
        print("Скрипт remove_firewall.sh успешно выполнен.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении remove_firewall.sh: {e}")

# run_remove_firewall()

#---------------------------------------------------------------------------------------
# Полная очистка правил nftable
# ВНИМАНИЕ /etc/nftables.conf не будет удалятся
def clear_firewall():
    confirm = input('Подтвердите вы уверены что хотите очистить firewall (Y/N) ')
    if confirm.lower() == 'y':
        try:
            # nft flush ruleset
            subprocess.run(["nft", "flush", "ruleset"], check=True)
            print("Правила успешно очищены.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении команды: {e}")
#---------------------------------------------------------------------------------------

def save_or_apply_rules_firewall():
    while True:
        print("1. Cохранить правила")
        print("2. Применить правила")
        print("3. Вернутся назад")
        num = int(input('Сделайте выбор сценария: '))
        if num == 1:
            try:
                subprocess.run(["bash", "./programs/save_rules.sh"], check=True)
                print("Скрипт save_or_apply_rules.sh успешно выполнен.")
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при выполнении save_rules.sh: {e}")
        elif num == 2:
            try:
                subprocess.run(["bash", "./programs/apply_rules.sh"], check=True)
                print("Скрипт apply_rules.sh успешно выполнен.")
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при выполнении apply_rules.sh: {e}")
        elif num == 3:
            break
        else:
            print('Некорректный выбор, попробуйте ещё раз.')

#--------------------------------------------------------------------------------------

def main():
    while True:
        print("\nМеню:")
        print("1. Важно для стабильной работы nftables! Удаление сторонних firewall (iptables, firewalld)")
        print("2. Очистить firewall (nftables)")
        print("3. Сохранить или применить правила в /etc/nftables.conf")
        print("4. Выйти")

        number = int(input('Сделайте выбор сценария: '))
        if number == 1:
            run_remove_firewall()
        elif number == 2:
            clear_firewall()
        elif number == 3:
             save_or_apply_rules_firewall()
        elif number == 4:
            print("Выход из программы.")
            break  # Выход
        else:
            print('Некорректный выбор, попробуйте ещё раз.')

# Запуск основной функции
main()
