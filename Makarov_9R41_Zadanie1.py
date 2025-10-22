
# данные от юзера
temp = int(input("Введите температуру: "))
is_rainy = input("Идет дождь? (да/нет): ").lower() == 'да'
is_raining_heavily = False
if is_rainy:
        is_raining_heavily = input("идет ливень? (да/нет): ").lower() == 'да'
 # выбора одежды
if temp < 0:
        print("Надень пуховик, шапку и шарф.")
elif temp < 10:
        print("Надень теплую куртку.")
elif temp < 15:
        print("Надень ветровку.")
elif temp < 20:
        print("Надень свитшот или худи.")
else:
        print("Можно надеть футболку.")

    # Допы для дождя
if is_raining_heavily:
            print("Возьми зонт и надень галоши.")
elif is_rainy:
            print("Возьми зонт.")
