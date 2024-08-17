import pandas as pd
from faker import Faker

fake = Faker()
data = {
    'Name': [fake.name() for _ in range(5)],
    'Address': [fake.address() for _ in range(5)],
    'Email': [fake.email() for _ in range(5)]
}

df = pd.DataFrame(data)
df.to_csv('simple_export.csv', index=False)
df.to_json('simple_export.json')
df.to_excel('simple_export.xlsx', index=False)
print(df)
