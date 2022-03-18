from Crypto.Cipher import AES
import glob
import time
import sys
password='abcdabcdabcdabcd'
iv=b'chromoglinowanie'

def pad(s):
    return s + ((16 - len(s) % 16) * chr(
        16 - len(s) % 16)).encode('utf-8')

def unpad(s):
    last_byte = s[-1]
    if last_byte > 16:
        return s
    if all(b == last_byte for b in s[16 - last_byte:]):
        return s[:16 - last_byte]
    return s




params = {
    'AES-128-ECB': [password, AES.MODE_ECB],
    'AES-128-CBC': [password, AES.MODE_CBC, iv],
    'AES-128-CFB': [password, AES.MODE_CFB, iv],
    'AES-128-OFB': [password, AES.MODE_OFB, iv],
    'AES-128-CTR': [password, AES.MODE_CTR, iv, lambda: iv],
    # 'AES-128-OPENPGP': [password, AES.MODE_OPENPGP, iv],
    # 'AES-128-CCM': [password, AES.MODE_CCM, iv],
    # 'AES-128-EAX': [password, AES.MODE_EAX, iv],
    # 'AES-128-GCM': [password, AES.MODE_GCM, iv],
    # 'AES-128-SIV': [password, AES.MODE_SIV, iv],
    # 'AES-128-OCB': [password, AES.MODE_OCB, iv],
}
results = {}
for algo in params:
    print(algo, file=sys.stderr)
    results[algo] = {}
    aes = AES.new(*params[algo])
    for file in glob.glob('texts/*.txt'):
        with open(file, 'rb') as f:
            data = pad(f.read())
            start_time = time.time()
            aes.encrypt(data)
            time_passed = time.time() - start_time
            results[algo][file] = time_passed
print(';'.join(['algo', *glob.glob('texts/*.txt')]))
for algo in results:
    print(';'.join([algo, *map(str, results[algo].values())]).replace('.', ','))