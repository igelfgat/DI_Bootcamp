from menu_item import MenuItem
import psycopg2

DBNAME = "Restaurant_Menu_Manager"
USER = "postgres"  # postgres
PASSWORD = "5859"  # <YOUR POSTGRES PASSWORD>
HOST = "localhost"
PORT = "5432"

connection = psycopg2.connect(
    dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
)

# 2. Create a cursor (tool to run queries)
cursor = connection.cursor()

class MenuManager:
    def get_by_name(name):
        query = "SELECT item_id, item_name, item_price FROM Menu_Items WHERE item_name = %s;"
        cursor.execute(query,(name,))
        result = cursor.fetchone()
        if result:
            item_id, name_item, price_item = result
            item = MenuItem(name_item, price_item)
            item.item_id = item_id
            return item
        else:
            return None
    
    def all_items():
        query = "SELECT item_id, item_name, item_price FROM Menu_Items;"
        cursor.execute(query)
        results = cursor.fetchall()
        items = []
        for result in results:
            item_id, name_item, price_item = result
            item = MenuItem(name_item, price_item)
            item.item_id = item_id
            items.append(item)
        return items
    
def main():
    item2 = MenuManager.get_by_name('Beef Stew')
    if item2:
        print(f"Found item: {item2.name_item} - {item2.price_item}")
    else:
        print("Item not found.")    
    items = MenuManager.all_items()
    for item in items:
        print(f"{item.item_id}: {item.name_item} - {item.price_item}")
if __name__ == "__main__":
    main()