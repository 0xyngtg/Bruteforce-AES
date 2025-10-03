# Bruteforce-AES
Python AES256-CBC bruteforce - using pyAesCrypt.

## Prerequisites
- Python3.6 or higher
- pip
- pyAesCrypt library

## Setup
1. Clone the repository.
```
git clone https://github.com/yourusername/aes-bruteforcer.git
cd aes-bruteforcer
```

2. Install pyAesCrypt(https://github.com/marcobellaccini/pyAesCrypt):
```
pip install pyAesCrypt
```

## Usage
```
python aes_bruteforcer.py -w <WORDLIST> -i <ENCRYPTED_FILE> -o <OUTPUT_FILE>
```
## Output Example
```
$ python3 script.py -w ~/wordlists/rockyou.txt -i encrypted.zip.aes -o decrypted.zip
[*] Testing passwords from "/home/kali/wordlists/rockyou.txt"!
[+] Password Found: password
[*] Time Taken: 11.74 seconds
```

## Disclaimer
This tool is intended for:
- Security research and education
