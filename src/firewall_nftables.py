#!/usr/bin/env python3

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


def clear_firewall():
    confirm = input('Подтвердите вы уверены что хотите очистить firewall (Y/N) ')
    if confirm.lower() == 'y':
        try:
            # Выполняем команду nft flush ruleset
            subprocess.run(["nft", "flush", "ruleset"], check=True)
            print("Правила успешно очищены.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении команды: {e}")





def main():
    print("\nМеню:")
    print("1. Очистить  firewall (nftables)")
    print("2. Показать применённые команды")
    print("3. Выйти")

main()

number = int(input('Сделайте выбор сценария: '))
if number == 1:
    clear_firewall()
else:
    print('Некорректный выбор, попробуйте ещё раз.')
