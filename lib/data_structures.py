spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """
    Takes a list of spicy_foods and returns a list of strings with the names of each spicy food.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Takes a list of spicy_foods and returns a list of dictionaries where the heat level is greater than 5.
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """
    Takes a list of spicy_foods and prints each spicy food in the format:
    Name (Cuisine) | Heat Level: 🌶🌶🌶...
    """
    for food in spicy_foods:
        peppers = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Takes a list of spicy_foods and a cuisine string, returns the dictionary 
    for the spicy food whose cuisine matches the given cuisine.
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    """
    Takes a list of spicy_foods and prints ONLY the spicy foods that have 
    a heat level greater than 5 in the same format as print_spicy_foods().
    Uses previously written functions.
    """
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    """
    Takes a list of spicy_foods and returns an integer representing 
    the average heat level of all the spicy foods.
    """
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_spicy_food):
    """
    Takes a list of spicy_foods and a new spicy_food dictionary,
    returns the original list with the new spicy_food added.
    """
    return spicy_foods + [new_spicy_food]