#!/usr/bin/env python
"""
This module generates fake insurance data that conforms to something you can find in real-life.
"""
import os
import subprocess
from datetime import datetime
import numpy as np
import pandas as pd
from faker import Faker

# create data based on schema
os.chdir(os.getcwd())

# instantiate faker with different locales
fake = Faker(["it_IT", "en_US", "en_GB"])

# create date size
# initialize dates
today = datetime.today().strftime("%Y-%m-%d")
start_date = datetime.strptime("2000-01-01", "%Y-%m-%d")
end_date = datetime.strptime(today, "%Y-%m-%d")
rand_dates = [
    datetime.strftime(
        fake.date_time_between_dates(start_date, end_date), "%Y-%m-%d %H:%M:%S"
    )
    for _ in range(1001)
]
rand_kra = [
    fake.bothify(text="?#########?", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for _ in range(1001)
]

# make random ids
customer_ids = list(range(1001))

# get data from wikipedia table
counties_kenya_page = pd.read_html("https://en.wikipedia.org/wiki/Counties_of_Kenya")
counties_capitals = counties_kenya_page[2][["County", "Capital"]]
counties_capitals = counties_capitals.dropna()
slice_counties = counties_capitals.iloc[:, 0]

# counting the counties
df = pd.DataFrame({"id": np.sort(customer_ids)})

# update the probabilities in the list to a non-random sample with variable p
# use dirichlet prob distribution too to enable the probabilities add up to one.
# you can also try dividing each entry by the sum of the array
df["County"] = np.random.choice(
    slice_counties,
    size=len(df),
    p=list(np.random.dirichlet(np.ones(len(slice_counties)))),
)
df["Gender"] = np.random.choice(["Male", "Female"], size=len(df), p=[0.49, 0.51])
df["Marital_status"] = np.random.choice(
    ["Single", "Divorced", "Married", "Widowed", "Separated", "Registered Partnership"],
    size=len(df),
    p=list(np.random.dirichlet(np.ones(6))),
)
df["No_of_dependents"] = np.random.choice(range(6), size=len(df))
df["Age"] = np.random.choice(range(30, 75), len(df))
df["Tier"] = np.random.choice(
    ["Bronze", "Silver", "Gold"], size=len(df), p=[0.5, 0.3, 0.2]
)
df["Policy_limit"] = np.random.choice(
    [300000, 500000, 1000000], size=len(df), p=[0.5, 0.3, 0.2]
)
df["Illness_category"] = np.random.choice(
    ["Congenital", "Acute", "Subacute", "Chronic"],
    size=len(df),
    p=[0.25, 0.25, 0.25, 0.25],
)
df["Date_of_entry"] = pd.to_datetime(rand_dates)
df["Updated_subscription"] = np.random.choice(
    ["Yes", "No"], size=len(df), p=[0.45, 0.55]
)
df["Account_withdrawal"] = np.random.choice(["Yes", "No"], size=len(df), p=[0.2, 0.8])
df["Retention"] = np.random.choice(range(1, 22), size=len(df))
df["ID_number"] = np.random.choice(range(1000000, 40000000), size=len(df))
df["Tax_id"] = rand_kra

# export to CSV
df.to_csv("Insurance_data_ke.csv", index=False)

# make it executable
# exec_code = subprocess.call("chmod a+x codebook.sh")

# use subprocess to run the sh file
EXIT_CODE = subprocess.call("./codebook.sh")
print(EXIT_CODE)
