# Generates sample contacts and deals CSVs for the HubSpot CRM project
# Install first: pip install faker pandas

import random
import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

sources = ["LinkedIn", "Website", "Referral", "Instagram"]
platforms = ["Shopify", "WooCommerce", "Other"]
stages = ["Appointment Scheduled", "Qualified To Buy", "Presentation Scheduled",
          "Decision Maker Bought-In", "Contract Sent", "Closed Won", "Closed Lost"]

contacts = []
for _ in range(30):
    contacts.append({
        "First Name": fake.first_name(),
        "Last Name": fake.last_name(),
        "Email": fake.unique.email(),
        "Company Name": fake.company(),
        "Lead Source": random.choice(sources),
        "Budget": random.randint(300, 5000),
        "Store Platform": random.choice(platforms)
    })
contacts_df = pd.DataFrame(contacts)
contacts_df.to_csv("contacts.csv", index=False)

deals = []
for c in random.sample(contacts, 15):
    deals.append({
        "Deal Name": c["Company Name"] + " Store Support",
        "Deal Stage": random.choice(stages),
        "Amount": c["Budget"],
        "Close Date": fake.date_between(start_date="today", end_date="+60d").strftime("%Y-%m-%d"),
        "Contact Email": c["Email"]
    })
deals_df = pd.DataFrame(deals)
deals_df.to_csv("deals.csv", index=False)

print(contacts_df.head())
print(deals_df.head())