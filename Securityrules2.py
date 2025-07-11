from pandevice import firewall
from pandevice import policies

import login_module
from login_module  import login
import csv

def main():
    try:
        fw=login_module.login()
        file_path=r"D:\Python_LAB\LAB9\lab9-rules.csv"
        csv_obj=open(file_path,"r")
        csv_reader=csv.reader(csv_obj)
        rulebase=policies.Rulebase()
        fw.add(rulebase)
        print("rulebase created ")

        security_rules=[]
        print('rules created into security_rule list :',security_rules)

        for row in csv_reader:
            print(row)
            rule_name=row[0]
            fromzone=row[1].split(" ")
            source =row[2].split(" ")
            tozone=row[3].split(" ")
            service=row[4].split(" ")
            application=row[5].split(" ")
            action=row[6]

            security_rules.append(policies.SecurityRule(
                name=rule_name,
                fromzone=fromzone,
                source = source,
                tozone = tozone,
                service = service,
                application = application,
                action = action)
            )
            print("rule created")
        print("commiting changes....")
        fw.commit()



    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

