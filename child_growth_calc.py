import math
import json
import robin_prompt

with open('data.json') as file:
    data = json.load(file)

def ChildPrompt():
    result = {
        "hp": 0,
        "str": 0,
        "mag": 0,
        "skl": 0,
        "spd": 0,
        "lck": 0,
        "def": 0,
        "res": 0
    }

    child_name = input("Choose a child unit:\n\n").lower()
    print("\n----------------------------------------\n")
    running = True
    while running:
        if child_name not in data["gen2"]:
            child_name = input(child_name.capitalize() + " is not a child unit, please try again:\n\n").lower()
            print("\n----------------------------------------\n")
        else:
            child = data["gen2"][child_name]
            running = False
    parent1 = data["gen1"][child["parent"]]
    parent2_name = input("Choose a parent:\n\n").lower()
    print("\n----------------------------------------\n")
    running = True
    while running:
        if parent2_name not in parent1["partners"]:
            parent2_name = input(parent2_name.capitalize() + " is not a compatible parent, please try again:\n\n").lower()
            print("\n----------------------------------------\n")
        else:
            parent2 = data["gen1"][parent2_name]
            running = False

    if parent1 == data["gen1"]["robin"]:
        parent1["growths"] = robin_prompt.RobinPrompt(parent1["growths"])
    elif parent2 == data["gen1"]["robin"]:
        parent2["growths"] = robin_prompt.RobinPrompt(parent2["growths"])
    
    child_class = input("Choose " + child_name.capitalize() + "'s class:\n\n").lower()
    print("\n----------------------------------------\n")
    running = True
    while running:
        if child_class not in child["classes"]:
            child_class = input(child_class.capitalize() + " is not a compatible class, please try again:\n\n").lower()
            print("\n----------------------------------------\n")
        else:
            running = False
    
    for stat in result:
        result[stat] = ((child["growths"][stat] + parent1["growths"][stat] + parent2["growths"][stat]) / 3) + data["classes"][child_class]["growths"][stat]
    
    print(child_name.capitalize() + "'s growth rates:\n")
    for stat in result:
        print(stat + ": " + str(math.floor(result[stat])))
    print("\n----------------------------------------\n")