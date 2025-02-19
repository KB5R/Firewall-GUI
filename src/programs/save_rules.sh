#!/bin/bash

HOME_DIR=$HOME/backup_firewall/iptables

IMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$HOME_DIR/iptables_backup_$TIMESTAMP.conf"

echo "Создаём бэкап /etc/iptables/rules.v4..."
cp /etc/iptables/rules.v4 "$BACKUP_FILE"
if [ $? -eq 0 ]; then
    echo "Бэкап успешно создан: $BACKUP_FILE"
else
    echo "Ошибка при создании бэкапа!"
    exit 1
fi
