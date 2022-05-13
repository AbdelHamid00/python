def print_recipe(name):
    print("ingredients of the recipe :", cookbook[name]['ingredients'])
    print("to be eaten for ", cookbook[name]['meal'])
    print("Takes ", cookbook[name]['prep_time'], "of cooking")

def delete_recipe(name):
    cookbook.pop(name)

def add_recipe(name, ingredients, meal, time):
    cookbook[name] = {}
    cookbook[name]['ingredients'] = ingredients.split(sep=' ')
    cookbook[name]['meal'] = meal
    cookbook[name]['time'] = time

cookbook = {'sandwich': {'ingredients': ['ham', 'bread', 'cheese'], 'meal': 'lunch', 'prep_time': '10minutes'}, \
'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': '60minutes'}, \
'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': '15minutes'}}
choice = input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>>')
if (choice == '1'):
    name = input("what is the name of the recipe ?\n>>")
    ingredients = input("what is the ingredients of this recipe ?\n>>")
    meal = input("When could this recipe be eaten?\n(lunch or dessert)\n>>")
    time = input("for how long?\n>>")
    add_recipe(name, ingredients, meal, time)
elif (choice == '2'):
    name = input("name of the recipe you want to delete?\n (space bethween avery single element.)\n>>")
    delete_recipe(name)
elif (choice == '3'):
    name = input("name of the recipe you want to print?\n>>")
    print_recipe('cake')
elif (choice == '4'):
    for a in cookbook:
        print("Name of the recipe : ",a)
        print_recipe(a)
        print("\n")
elif (choice == '5'):
    print("Cookbook closed.\n")
    exit()
else:
    print("This option does not exist, please type the corresponding number.")

