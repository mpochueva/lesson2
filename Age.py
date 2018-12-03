def occupation(user_age):
    occup = ""
    if 0 <= user_age < 7:
        occup = "Вам в детский сад"
    elif 7 <= user_age < 18:
        occup = "Вам в школу"
    elif 18 <= user_age < 23:
        occup = "Вам в ВУЗ"
    else:
        occup = "Работать!"
    return occup


age = input("Ваш возраст (полных лет)?")
print(occupation(int(age)))

