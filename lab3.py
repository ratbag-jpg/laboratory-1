# Каталог товарів
products = {
    "Хліб": {"price": 25.50, "stock": 10},
    "Молоко": {"price": 42.99, "stock": 8},
    "Сік": {"price": 55.75, "stock": 5}
}

cart = []

# Лямбда для форматування ціни
format_price = lambda price: f"{price:.2f} грн"

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
        print("\nКаталог:")
        for name, info in products.items():   #перебираємо товари
            print(f"{name} - {format_price(info['price'])}")  #  показує назву + ціну

    elif choice == "2":
        item = input("Назва товару: ")
        if item in products and products[item]["stock"] > 0:  #чи існує товар і чи є він на складі
            cart.append(item)  #додає товар в кошик
            print("Товар додано.")
        else:
            print("Товар відсутній.")

    elif choice == "3":
        item = input("Назва товару: ")
        if item in cart:  #перевіряє наявність товару в кошику
            cart.remove(item)  #видаляє товар з кошика
            print("Товар видалено.")
        else:
            print("Товару немає в кошику.")

    elif choice == "4":
        if not cart:  #перевіряє чи кошик порожній
            print("Кошик порожній.")
        else:
            total = sum(products[item]["price"] for item in cart)  #обчислює суму товарів
            print("Кошик:", cart)
            print("Сума:", format_price(total))

    elif choice == "5":
        if not cart:
            print("Кошик порожній.")
        else:
            total = sum(products[item]["price"] for item in cart)

            for item in cart:  #перебирає товари в кошику
                products[item]["stock"] -= 1  #віднімає 1 значення з складу

            print("Покупку завершено.")
            print("До сплати:", format_price(total)) #фулл сума
            cart.clear()  # очищує корзину

    elif choice == "6":
        login = input("Логін: ")
        password = input("Пароль: ")

        if login == "admin" and password == "1234":  #перевіряє правильність данних
            print("\nЗалишки товарів:")
            for name, info in products.items():  #перебирає товари
                print(f"{name}: {info['stock']} шт.")  #показує залтшок товару
        else:
            print("Невірний логін або пароль.")

    elif choice == "0":
        break

    else:
        print("Невірний вибір.")