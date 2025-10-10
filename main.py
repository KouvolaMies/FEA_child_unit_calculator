import math
import json
import robin_prompt

with open('data.json') as file:
    data = json.load(file)


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

def ChildPrompt():
    child = input("Choose a child unit: ")
    running = True
    while running:
        if child not in data["gen2"]:
            child = input(child + " is not a child unit, please try again: ")
        else:
            child = data["gen2"][child]
            running = False
    parent1 = data["gen1"][child["parent"]]
    parent2 = input("Choose a parent: ")
    running = True
    while running:
        if parent2 not in parent1["partners"]:
            parent2 = input(parent2 + " is not a compatible parent, please try again: ")
        else:
            parent2 = data["gen1"][parent2]
            running = False

    if parent1 == data["gen1"]["robin"]:
        parent1["growths"] = robin_prompt.RobinPrompt(parent1["growths"])
    elif parent2 == data["gen1"]["robin"]:
        parent2["growths"] = robin_prompt.RobinPrompt(parent2["growths"])
    
    child_class = input("Choose the child unit's class: ")
    running = True
    while running:
        if child_class not in child["classes"]:
            child_class = input(child_class + " is not a compatible class, please try again: ")
        else:
            running = False
    
    for stat in result:
        result[stat] = ((child["growths"][stat] + parent1["growths"][stat] + parent2["growths"][stat]) / 3) + data["classes"][child_class]["growths"][stat]

ChildPrompt()

for stat in result:
    print(stat + ": " + str(math.floor(result[stat])))