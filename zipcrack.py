import zipfile
from tqdm import tqdm

wordlist = input("Enter Password list: ")

zip_file = input("Enter zip file: ")

#
zip_file = zipfile.ZipFile(zip_file)


print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password cracked:", word.decode().strip())
            exit(0)
print("[!] Invalid password.")
