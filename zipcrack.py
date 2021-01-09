import zipfile
from tqdm import tqdm

# the password list path you want to use, must be available in the current directory
wordlist = input("Enter Password list: ")
# the zip file you want to crack its password
zip_file = input("Enter zip file: ")

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
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