#!/bin/bash

BACKUP_DIR="/root/firewall_backup_$(date +%Y%m%d_%H%M%S)"

mkdir -p "$BACKUP_DIR"

echo "Проверка iptables..."
if command -v iptables >/dev/null 2>&1; then
    echo "iptables установлен, создаю резервную копию..."
    if [ -f /etc/sysconfig/iptables ]; then
        cp /etc/sysconfig/iptables "$BACKUP_DIR/"
    fi
    if [ -d /etc/iptables ]; then
        cp -r /etc/iptables "$BACKUP_DIR/"
    fi

    echo "Удаляю iptables..."
    if command -v apt >/dev/null 2>&1; then
        apt remove --purge -y iptables iptables-persistent
    elif command -v dnf >/dev/null 2>&1; then
        dnf remove -y iptables iptables-services
    elif command -v yum >/dev/null 2>&1; then
        yum remove -y iptables iptables-services
    else
        echo "Не удалось определить пакетный менеджер!"
        exit 1
    fi
else
    echo "iptables не установлен."
fi

echo "Проверка firewalld..."
if systemctl is-active --quiet firewalld || systemctl is-enabled --quiet firewalld || rpm -q firewalld >/dev/null 2>&1; then
    echo "firewalld установлен, создаю резервную копию..."
    if [ -d /etc/firewalld ]; then
        cp -r /etc/firewalld "$BACKUP_DIR/"
    fi

    echo "Останавливаю и удаляю firewalld..."
    systemctl stop firewalld
    systemctl disable firewalld

    if command -v dnf >/dev/null 2>&1; then
        dnf remove -y firewalld
    elif command -v yum >/dev/null 2>&1; then
        yum remove -y firewalld
    elif command -v apt >/dev/null 2>&1; then
        apt remove --purge -y firewalld
    else
        echo "Не удалось определить пакетный менеджер!"
        exit 1
    fi
else
    echo "firewalld не установлен."
fi

echo "Все завершено. Резервные копии сохранены в $BACKUP_DIR"

systemctl start nftables && systemctl enable nftables
