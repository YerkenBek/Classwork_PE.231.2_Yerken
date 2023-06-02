def show_manty_ing(total_kg=1):
    meat    = 0.5 * total_kg
    flour   = 0.2 * total_kg
    carrot  = 0.05 * total_kg
    pumpkin = 0.1 * total_kg
    onion   = 0.1 * total_kg
    potato  = 0.1 * total_kg
    template = """To prepare %s kg manty you will need:
    - мясо: %.2f кг,
    - мука: %.2f кг,
    - морковь: %.2f кг,
    - тыква: %.2f кг,
    - лук: %.2f кг,
    - картофель: %.2f кг.
    """
    message = template % (total_kg, meat, flour, carrot, pumpkin, onion, potato)
    print(message)
    return int(total_kg * 4) # number of portions

user_in = input("How many kg of mantys do you need? ")
user_kg = float(user_in)

portions = show_manty_ing(user_kg)
print("Total portions done:", portions)

