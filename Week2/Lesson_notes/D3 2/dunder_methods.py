class Table:
    def __init__(
        self, color: str, price: int
    ):  # Dunder method for initialization of objects
        self.color = color
        self.price = price

    def __str__(self) -> str:  # str()
        object_str = f"{self.color} Table, price - {self.price}"
        return object_str

    def __lt__(self, other: "Table") -> bool:  # < - less than operator
        return self.price < other.price

    def __gt__(self, other: "Table") -> bool:  # > - greater than operator
        return self.price > other.price


if __name__ == "__main__":
    table1 = Table("Brown", 100)
    print(table1)

    table1_str = str(table1)
    print(table1_str)

    table2 = Table("Yellow", 50)

    # print(table1 > table2)

    table3 = Table("Black", 125)
    table4 = Table("Yellow", 90)

    # print(table1 < table2)

    tables = [table2, table4, table3, table1]
    #  50,     90   ,   125 , 100

    tables.sort()

    for table in tables:
        print(table)
