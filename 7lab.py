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
orders = [InternetOrder(1, {'surname': 'A', 'product': 'B', 'quantity': 'C', 'price': '100', 'date': '2020-02-18'})]
def find(order_id, key):
    for order in orders:
        if order.order_id == order_id:
            try:
                return order.order_info[key]
            except KeyError:
                return "Wrong key"
    return "No such order"
def add_new_order(order_info):
    orders.append(InternetOrder(orders[-1].order_id + 1, order_info))
def delete_order(order_id):
    for order in orders:
        if order.order_id == order_id:
            orders.remove(order)
            return "Removed"
    return "No such order"
def get_order(order_id):
    for order in orders:
        if order.order_id == order_id:
            return order
    return "No such order"
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
        order_info = {'surname': input('Enter surname: '),
                      'product': input('Enter product name: '),
                      'quantity': input('Enter quantity: '),
                      'price': input('Enter price: '),
                      'date': input('Enter date: ')}
        add_new_order(order_info)
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
while True:
    run()
