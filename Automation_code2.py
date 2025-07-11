#!/usr/bin/env python
from pandevice import firewall
from pandevice import policies
from pandevice import objects
import csv

# Main function
if __name__ == '__main__':
    try:
        # Firewall credentials and CSV file
        user_name = "admin"
        password = "admin"
        firewall_ip = "192.168.1.100"
        csv_file_path = r"D:\Python_LAB\LAB9\lab9-rules-with-headers.csv"

        # Connect to the firewall
        fw = firewall.Firewall(hostname=firewall_ip, username=user_name, password= password)
        print("Connected to the firewall.")


        # Create an empty rulebase
        rulebase = policies.Rulebase()
        fw.add(rulebase)

        # Valid applications (update this list)
        valid_applications = ['web-browsing', 'dns', 'ssl', 'ssh', 'ping', 'smtp']

        # Read rules from CSV
        with open(csv_file_path, 'r') as file_:
            csv_reader = csv.reader(file_)
            next(csv_reader)  # Skip header

            for row in csv_reader:
                try:
                    rule_name, src_zone, src_ip, dst_zone, dst_ip, app, service, action = row
                    application = app.split(" ")

                    # Validate application names
                    if any(a not in valid_applications for a in application):
                        print(f"Invalid application in rule '{rule_name}': {application}. Skipping.")
                        continue

                    # Create and add rule
                    rule = policies.SecurityRule(
                        name=rule_name,
                        fromzone=[src_zone],
                        source=[src_ip],
                        tozone=[dst_zone],
                        destination=[dst_ip],
                        application=application,
                        service=service.split(" "),
                        action=action
                    )
                    rulebase.add(rule)
                    print(f"Rule '{rule_name}' added successfully.")
                except Exception as e:
                    print(f"Error processing rule {row}: {e}")

        # Commit changes
        print("Committing changes...")
        fw.commit()
        print("Rules committed successfully.")

    except Exception as e:
        print(f"Error: {e}")

