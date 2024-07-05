import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:5859@localhost/Customer_support_ticket_dataset')
df = pd.read_csv('Week4/Day4/customer_support_tickets.csv')

df.to_sql('customer_support_tickets', engine, if_exists='replace', index=False)