echo "Применяем правила из /etc/nftables.conf..."
nft -f /etc/nftables.conf
systemctl restart nftables
echo "Правила успешно применены."
