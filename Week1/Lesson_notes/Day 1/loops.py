# for loop
for _ in range(10):
    print("Hello")

for char in "Hello":
    print(char)
    
    
user_number = input("Provide a number here: ")
user_number = int(user_number)

# while loop
while user_number < 10:
    user_number = input("Provide a number here: ")
    user_number = int(user_number)

print(f"Number {user_number} is higher than 10")


print("A" not in "BAASADA") # False
print("A" in "BAASADA") # True
