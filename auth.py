from pandevice import firewall

def login():

    hostname = str(input("Enter Hostname"))
    username = str(input("Enter username"))
    password = str(input("Enter Password"))

    creds = {"admin": "admin", "admin1": "admin1"}
    if username in creds and creds[username] == password:
        print(f"Authentication is Sucessful")
        fw = firewall.Firewall(username=username, password=password, hostname=hostname)
        print(f"Connected to {hostname}")
    else:
        print("Invalid Creds!")
    return fw