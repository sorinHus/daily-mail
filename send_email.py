import csv
import os
from datetime import date
import urllib.request
import json

TODAY = date.today().isoformat()
RESEND_API_KEY = os.environ["RESEND_API_KEY"]
TO_EMAIL = "sorin.v.hus@gmail.com"
FROM_EMAIL = "sorin@487.ro"

def send():
    with open("emails.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"] == TODAY:
                payload = json.dumps({
                    "from": FROM_EMAIL,
                    "to": [TO_EMAIL],
                    "subject": row["subject"],
                    "text": row["body"]
                }).encode("utf-8")

                req = urllib.request.Request(
                    "https://api.resend.com/emails",
                    data=payload,
                    headers={
                        "Authorization": f"Bearer {RESEND_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    method="POST"
                )
                try:
                    with urllib.request.urlopen(req) as resp:
                        print(f"Sent: {row['subject']} - status {resp.status}")
                except urllib.error.HTTPError as e:
                    body = e.read().decode()
                    print(f"Error {e.code}: {body}")
                    raise
                return

    print(f"No email found for {TODAY}")

send()
