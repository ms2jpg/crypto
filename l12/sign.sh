#mkdir -p a
#mkdir -p b
#python3 generate.py a
#python3 generate.py b

python3 encrypt.py a/id_rsa message.txt encrypted_a.bin
python3 encrypt.py b/id_rsa message.txt encrypted_b.bin

python3 decrypt.py a/id_rsa.pub encrypted_a.bin message_a.txt
python3 decrypt.py b/id_rsa.pub encrypted_b.bin message_b.txt

md5sum message_*.txt
