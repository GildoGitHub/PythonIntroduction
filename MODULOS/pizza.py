def make_pizza(size, *toppings):
    print("Meking a "+str(size)+" inch pizzas with the following topping: ")
    for topping in toppings:
        print("-"+topping)
