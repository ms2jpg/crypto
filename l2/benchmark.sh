# Reset
CLEAR='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White

input_file=payload.txt
password=abcdabcdabcdabcd
iv=chromoglinowanie

echo -e "${BBlue}==================== AES-ECB ====================$CLEAR"
echo -e "${BGreen}encrypting$Green: $input_file -> aes_ecb_encrypted$CLEAR"
python3 main.py -e -m aes-ecb -i $input_file -o aes_ecb_encrypted -p $password -v
echo -e "\n${BRed}decrypting$Red: aes_ecb_encrypted -> aes_ecb_decrypted$CLEAR"
python3 main.py -d -m aes-ecb -i aes_ecb_encrypted -o aes_ecb_decrypted -p $password -v

echo -e "\n${BYellow}Checksums$CLEAR"
md5sum $input_file aes_ecb_decrypted

echo -e "\n\n${BCyan}==================== AES-CBC ====================$CLEAR"
echo -e "${BGreen}encrypting$Green: $input_file -> aes_cbc_encrypted$CLEAR"
python3 main.py -e -m aes-cbc -i $input_file -o aes_cbc_encrypted -p $password -v -iv $iv -ivt raw
echo -e "\n${BRed}decrypting$Red: aes_cbc_encrypted -> aes_cbc_decrypted$CLEAR"
python3 main.py -d -m aes-cbc -i aes_cbc_encrypted -o aes_cbc_decrypted -p $password -v -iv $iv -ivt raw

echo -e "\n${BYellow}Checksums$CLEAR"
md5sum $input_file aes_cbc_decrypted

echo -e "\n\n${BPurple}==================== AES-CTR ====================$CLEAR"
echo -e "${BGreen}encrypting$Green: $input_file -> aes_ctr_encrypted$CLEAR"
python3 main.py -e -m aes-ctr -i $input_file -o aes_ctr_encrypted -p $password -v -iv $iv -ivt raw
echo -e "\n${BRed}decrypting$Red: aes_ctr_encrypted -> aes_ctr_decrypted$CLEAR"
python3 main.py -d -m aes-ctr -i aes_ctr_encrypted -o aes_ctr_decrypted -p $password -v -iv $iv -ivt raw

echo -e "\n${BYellow}Checksums$CLEAR"
md5sum $input_file aes_ctr_decrypted