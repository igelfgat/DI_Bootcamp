# pip install faker
from faker import Faker


fake_data_generator = Faker()

last_name_russian = fake_data_generator.last_name()

print(last_name_russian)
