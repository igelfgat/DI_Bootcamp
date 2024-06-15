name = "Yossi"
age = 33

if name == "Yossi":
    print(f"Hello {name}")
elif age > 30:
    print(f"Your age is higher than 30")
elif name == "Ben" and age == 10:
    print(f"Hi {name}, go to school.")
else:
    print("I dont recognise you - Terminating") 
    
    
    
sky_color = "Red"
print((10 < 20) or (sky_color == "Blue"))
# or - needs at least one condition to return True to result in True 

print((10 < 20) and (sky_color == "Blue"))
# and - needs at least one condition to return False to result in False 