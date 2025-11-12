temperature = float(input("Какая температура на улице? "))

if temperature <= 0:
    print("Пуховик")

elif 20 < temperature < 30:
    is_rainy_input = input("Идет дождь? (да/нет): ")
    is_rainy = (is_rainy_input.lower() == "да")
    if is_rainy:
        print("Футболка, шорты и дождевик")
    else:
        print("Футболка и шорты")

else:
    is_rainy_input = input("Идет дождь? (да/нет): ")
    is_rainy = (is_rainy_input.lower() == "да")
    if is_rainy:
        is_raining_heavily_input = input("Дождь сильный? (да/нет): ")
        is_raining_heavily = (is_raining_heavily_input.lower() == "да")
        if is_raining_heavily:
            print("Пальто, резиновые сапоги и зонт")
        else:
            print("Пальто и дождевик")
    else:
        print("Пальто")
