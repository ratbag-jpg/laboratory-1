users = ["ilya", "vadym", "anna", "oleg"]
passwords = ["1234", "1111", "2222", "3333"]
grades = [
    [12, 10, 8, 5, 3],
    [7, 9, 11, 4, 6],
    [4, 5, 8, 10, 12],
    [1, 2, 4, 7, 9]
]

login = input("Логін: ")
password = input("Пароль: ")

if login in users and password == passwords[users.index(login)]:
    i = users.index(login)
    print("Оцінки:", grades[i])

    good = 0
    bad = 0

    for grade in grades[i]:
        if grade >= 5:
            good += 1
        else:
            bad += 1

    print("Задовільних:", good)
    print("Незадовільних:", bad)
else:
    print("Неправильний логін або пароль")