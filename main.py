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
    child = input("Choose a child unit:\n")
    child = data["gen2"][child]
    parent1 = data["gen1"][child["parent"]]
    parent2 = input("Choose a parent:\n")
    parent2 = data["gen1"][parent2]

    if parent1 == data["gen1"]["robin"]:
        parent1["growths"] = robin_prompt.RobinPrompt(parent1["growths"])
    elif parent2 == data["gen1"]["robin"]:
        parent2["growths"] = robin_prompt.RobinPrompt(parent2["growths"])
    
    child_class = input("Choose the child unit's class:\n")
    running = True
    while running:
        if child_class not in child["classes"]:
            child_class = input("Please choose a compatible class:\n")
        else:
            running = False
    
    for stat in result:
        result[stat] = ((child["growths"][stat] + parent1["growths"][stat] + parent2["growths"][stat]) / 3) + data["classes"][child_class]["growths"][stat]

ChildPrompt()

for stat in result:
    print(stat + ": " + str(math.floor(result[stat])))