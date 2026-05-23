import csv
import os
import resend
from datetime import date

TODAY = date.today().isoformat()
resend.api_key = os.environ["RESEND_API_KEY"]

def send():
    with open("emails.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"] == TODAY:
                params = {
                    "from": "sorin@487.ro",
                    "to": ["sorin.v.hus@gmail.com", "oana314@gmail.com"],
                    "subject": row["subject"],
                    "text": row["body"],
                }
                email = resend.Emails.send(params)
                print(f"Sent: {email}")
                return
    print(f"No email found for {TODAY}")

send()
