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



password=abcdabcdabcdabcd
iv=chromoglinowanie
path=$1
filename=$(echo $path | awk -F/ '{print $2}')
algo=$(echo $filename | grep -o "aes-[^-_]*")

python3 main.py -d -m $algo -i $path -o decrypted/$filename -p $password -iv $iv -ivt raw;

#for file in $(ls raw/); do
#  new_filename=$(echo $file | awk -F. '{print $1}')
#  python3 main.py -e -m aes-ecb -i raw/$file -o encrypted/$new_filename-aes-ecb.enc -p $password;
#  python3 main.py -e -m aes-cbc -i raw/$file -o encrypted/$new_filename-aes-cbc.enc -p $password -iv $iv -ivt raw;
#  python3 main.py -e -m aes-ctr -i raw/$file -o encrypted/$new_filename-aes-ctr.enc -p $password -iv $iv -ivt raw;
#done