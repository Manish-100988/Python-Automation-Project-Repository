from pandevice import firewall

def login():
    hostname = str(input("Enter Hostname\t:"))
    username = str(input("Enter  username\t:"))
    password = str(input("Enter  password\t:"))

    creds = {"admin1": "admin1", "admin2": "admin2"}
    if username in creds and creds[username] == password:
        fw = firewall.Firewall(username=username, password=password, hostname=hostname)
        print(f"loggedin into {hostname}")
    return fw


