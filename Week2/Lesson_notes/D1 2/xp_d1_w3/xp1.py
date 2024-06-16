class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Instantiate three Cat objects using the code provided above.


# Outside of the class, create a function that finds the oldest cat and returns the cat.


# APPROACH 1 - using for loop
def get_oldest_cat(cat_list: list[Cat]) -> Cat:

    oldest_cat = cat_list[0]

    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    return oldest_cat


# APPROACH 2 - using the max function
## create an extractor function
def get_cat_age(cat: Cat) -> int:
    return cat.age


def main():
    cat1 = Cat("Mizzy", 10)
    cat2 = Cat("Victoria", 8)
    cat3 = Cat("Lali", 6)

    cats = [cat1, cat2, cat3]
    #   10      8     6

    # Approach 1 solution
    # oldest_cat = get_oldest_cat(cats)

    # Approach 2 solution
    oldest_cat = max(cats, key=get_cat_age)  # regular function approach
    oldest_cat = max(cats, key=lambda cat: cat.age)  # Lambda function approach

    print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


if __name__ == "__main__":
    main()
