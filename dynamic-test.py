airmon-ng start wlan1
sleep 5
airbase-ng -e "seu-free" wlan1mon &
sleep 5
ifconfig at0 up
ifconfig at0 10.0.0.1 netmask 255.255.255.0
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -P FORWARD ACCEPT
iptables --append FORWARD --in-interface at0 -j ACCEPT
iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE
iptables -A FORWARD -p tcp --syn -s 10.0.0.0/24 -j TCPMSS  --clamp-mss-to-pmtu
dhcpd -cf /etc/dhcp/dhcpd.conf at0