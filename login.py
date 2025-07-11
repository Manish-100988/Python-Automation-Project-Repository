from pandevice import  firewall
from pandevice import policies
import csv

import login2
from login2 import login

def main():
    try:
        #user authentication

            fw=login2.login()


            #rule base and add into firewall
            rulebase=policies.Rulebase
            fw.add(rulebase)

            #assign csv_path,open csv,read csv file
            csvpath=r"D:\csv\csv_file.csv"
            opencsv=open(csvpath,"r")
            readcsv=csv.reader(opencsv)

            #rulelist
            rulelist=[]

            #"iterate rows in csv file"
            for row in readcsv:
                name=row[0]
                fromzone=row[1].split(" ")
                source = row[2].split(" ")
                tozone = row[3].split(" ")
                destination=row[4].split(" ")
                service = row[5].split(" ")
                application = row[6].split(" ")
                action = row[7]

                rulelist.append(policies.SecurityRule(name=name,
                                                  fromzone=fromzone,
                                                  source=source,
                                                  tozone=tozone,
                                                  destination=destination,
                                                  service=service,
                                                  application=application,
                                                  action=action))
                print(f"Rule created successfully :->{row}")






    except Exception as e:
        print(e)
if __name__=="__main__":
    main()

