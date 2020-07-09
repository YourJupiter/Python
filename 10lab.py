from sqlite3 import *

connection = connect('database.db')
cursor = connection.cursor()


class InternetOrder:
    def __init__(self, order_id, order_info):
        self.order_id = order_id
        self.order_info = order_info

    def __str__(self):
        return f'ID: {self.order_id}\n' \
               f'Surname: {self.order_info["surname"]}\n' \
               f'Product: {self.order_info["product"]}\n' \
               f'Quantity: {self.order_info["quantity"]}\n' \
               f'Price: {self.order_info["price"]}\n' \
               f'Date: {self.order_info["date"]}\n'


def start_db():
    cursor.execute("CREATE TABLE orders (id text, surname text, product text, quantity text, price text, date text)")


def find(order_id, key):
    order = get_order(order_id)
    try:
        return order.order_info[key]
    except KeyError:
        return 'Wrong key'


def add_new_order(order_id, order_info):
    order = InternetOrder(order_id, order_info)
    cursor.execute(f"""INSERT INTO orders VALUES (
                    '{order.order_id}',
                    '{order.order_info["surname"]}',
                    '{order.order_info["product"]}',
                    '{order.order_info["quantity"]}',
                    '{order.order_info["price"]}',
                    '{order.order_info["date"]}')""")
    connection.commit()


def delete_order(order_id):
    cursor.execute(f"DELETE FROM orders WHERE id={order_id}")
    connection.commit()


def get_order(order_id):
    cursor.execute(f"SELECT * FROM orders WHERE id={order_id}")
    rows = cursor.fetchall()
    data = rows[0]
    order = InternetOrder(data[0], {'surname': data[1],
                                    'product': data[2],
                                    'quantity': data[3],
                                    'price': data[4],
                                    'date': data[5]})
    return order


def run():
    menu = ['1. Add new order',
            '2. Delete order',
            '3. Get order by id',
            '4. Find in order',
            '5. Exit']
    for option in menu:
        print(option)
    option = input("Choose: ")
    if option == '1':
        order_id = input('Enter id: ')
        order_info = {'surname': input('Enter surname: '),
                      'product': input('Enter product name: '),
                      'quantity': input('Enter quantity: '),
                      'price': input('Enter price: '),
                      'date': input('Enter date: ')}
        add_new_order(order_id, order_info)
    elif option == '2':
        delete_order(int(input('Enter order id: ')))
    elif option == '3':
        print(get_order(int(input('Enter order id: '))))
    elif option == '4':
        print(find(int(input('Enter order id: ')), input('Enter key: ')))
    elif option == '5':
        exit()
    else:
        print("No such option")


try:
    start_db()
except OperationalError:
    pass
while True:
    run()
