products = {
    "Хліб": {"price": 25.50, "stock": 10},
    "Молоко": {"price": 42.99, "stock": 8},
    "Сік": {"price": 55.75, "stock": 5}
}

cart = []

# Лямбда для форматування ціни
format_price = lambda price: f"{price:.2f} грн"

# Функція для показу каталогу
def show_catalog():
    print("\nКаталог:")
    for name, info in products.items():
        print(f"{name} - {format_price(info['price'])}")

while True:
    print("\n1 - Каталог")
    print("2 - Додати в кошик")
    print("3 - Видалити з кошика")
    print("4 - Переглянути кошик")
    print("5 - Купити товари")
    print("6 - Адміністратор")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_catalog()

    elif choice == "2":
        item = input("Назва товару: ")

        if item in products and products[item]["stock"] > 0: #перевіпяє чи існує товар і чи є він на складі
            cart.append(item) #додає товар до кошика
            print("Товар додано.")
        else:
            print("Товар відсутній.")

    elif choice == "3":
        item = input("Назва товару: ")

        if item in cart: #перевіряє чи товар у кошику
            cart.remove(item) #видаляє товар з кошика
            print("Товар видалено.")
        else:
            print("Товару немає в кошику.")

    elif choice == "4":
        if not cart:  #перевіряє чи кошик порожній
            print("Кошик порожній.")
        else:
            total = sum(products[item]["price"] for item in cart) #обчислює загальну суму

            print("Кошик:", cart)
            print("Сума:", format_price(total))

    elif choice == "5":
        if not cart:
            print("Кошик порожній.")
        else:
            total = sum(products[item]["price"] for item in cart) #рахує суму

            for item in cart:
                products[item]["stock"] -= 1 #прибирає 1 товар з складу

            print("Покупку завершено.")
            print("До сплати:", format_price(total))

            cart.clear() #повністю очищує корзину

    elif choice == "6":
        login = input("Логін: ")
        password = input("Пароль: ")

        if login == "admin" and password == "1234": #перевіряє правильність логіна і пароля
            print("\nЗалишки товарів:")

            for name, info in products.items(): #перебирає товари
                print(f"{name}: {info['stock']} шт.")
        else:
            print("Невірний логін або пароль.")

    elif choice == "0":
        break

    else:
        print("Невірний вибір.")
