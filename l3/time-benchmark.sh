for algo in aes-128-ecb aes-128-cbc aes-128-ctr aes-128-cfb aes-128-ofb aes-128-pcb aes-128-bc aes-128-pcbc aes-128-ofbnlf aes-128-pfb aes-128-cbcc; do
  openssl speed -engine padlock -evp $algo 2> /dev/null | grep $algo
done