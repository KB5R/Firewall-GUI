#!/bin/bash

HOME_DIR=$HOME/backup_firewall/nftables

IMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$HOME_DIR/nftables_backup_$TIMESTAMP.conf"

echo "Создаём бэкап /etc/nftables.conf..."
cp /etc/nftables.conf "$BACKUP_FILE"
if [ $? -eq 0 ]; then
    echo "Бэкап успешно создан: $BACKUP_FILE"
else
    echo "Ошибка при создании бэкапа!"
    exit 1
fi

# 2. Очищаем файл /etc/nftables.conf
echo "Очищаем /etc/nftables.conf..."
echo > /etc/nftables.conf
if [ $? -eq 0 ]; then
    echo "Файл /etc/nftables.conf очищен."
else
    echo "Ошибка при очистке файла!"
    exit 1
fi


# 3. Сохраняем текущие правила в /etc/nftables.conf
echo "Сохраняем текущие правила nftables в /etc/nftables.conf..."
nft list ruleset > /etc/nftables.conf
if [ $? -eq 0 ]; then
    echo "Правила успешно сохранены в /etc/nftables.conf."
else
    echo "Ошибка при сохранении правил!"
    exit 1
fi
