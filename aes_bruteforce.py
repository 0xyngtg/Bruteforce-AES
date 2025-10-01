import pyAesCrypt
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import argparse

parser= argparse.ArgumentParser(
    prog= "aes_bruteforcer.py",
    description= "A simple tool that performs a brute-force attack against an AES encrypted file.",
    add_help= True
)
parser.add_argument(
    "-w", "--wordlist",
    help= "Passwords Wordlist",
    required= True
)

parser.add_argument(
    "-i", "--infile",
    help= "Encrypted file",
    required= True
)

parser.add_argument(
    "-o", "--outfile",
    help= "Out File",
    required= True
)

args= parser.parse_args()

found_event= threading.Event()

def decrypt(password):
    if found_event.is_set():
        return None
    try:
        pyAesCrypt.decryptFile(infile, outfile, password)
        return password
    except ValueError:
        return None
    except Exception as e:
        print(f"[-] Error: {e}")
        return None

def run_threads():
    i= 0
    batch_size= 100
    
    with ThreadPoolExecutor(max_workers= 5) as executor:
        with open(wordlist, "rt", encoding= "latin-1") as f:
            while True:
                futures= []
                
                for _ in range(batch_size):
                    line= f.readline()
                    if not line:
                        break
                    
                    password= line.strip()
                    if password:
                        future= executor.submit(decrypt, password)
                        futures.append(future)
                        
                        i+= 1
                        if i%1000== 0:
                            print(f"[*] Passwords tried: {i}")
                
                    if future.result() is not None:
                        found_event.set()
                        return future.result()
                
                if not futures and future.result()== None:
                    print("[-] Password not found!")
                    break
                
                if not found_event.is_set():
                    time.sleep(0.1)

if __name__ == "__main__":
    wordlist= args.wordlist
    infile= args.infile
    outfile= args.outfile
    
    print(f"[*] Testing passwords from \"{wordlist}\"!")
    
    start_time= time.time()
    result= run_threads()
    end_time= time.time()
    
    if result:
        print(f"[+] Password Found: {result}")
        print(f"[*] Time Taken: {end_time - start_time:.2f} seconds")
    else:
        print("[-] Password not found!")
