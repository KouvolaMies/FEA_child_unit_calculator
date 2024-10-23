import math
chrom = {
    "hp": 45,
    "str": 40,
    "mag": 10,
    "skl": 40,
    "spd": 40,
    "lck": 70,
    "def": 35,
    "res": 20
}
robin = {
    "hp": 40,
    "str": 40,
    "mag": 35,
    "skl": 35,
    "spd": 35,
    "lck": 55,
    "def": 30,
    "res": 20
}
sully = {
    "hp": 40,
    "str": 35,
    "mag": 20,
    "skl": 40,
    "spd": 40,
    "lck": 60,
    "def": 35,
    "res": 20
}
lucina = {
    "hp": 45,
    "str": 35,
    "mag": 20,
    "skl": 45,
    "spd": 45,
    "lck": 80,
    "def": 25,
    "res": 25
}
lord = {
    "hp": 40,
    "str": 20,
    "mag": 0,
    "skl": 20,
    "spd": 20,
    "lck": 0,
    "def": 10,
    "res": 5
}
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

for stat in result:
    result[stat] = ((chrom[stat] + sully[stat] + lucina[stat]) / 3) + lord[stat]

for stat in result:
    print(stat + ": " + str(math.floor(result[stat])))

def RobinPrompt():
    #reset robin's stats
    robin["hp"] = 40
    robin["str"] = 40
    robin["mag"] = 35
    robin["skl"] = 35
    robin["spd"] = 35
    robin["lck"] = 55
    robin["def"] = 30
    robin["res"] = 20

    asset = input("choose robin's asset: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
    running = 1
    while running == 1:
        if asset == "1":
            robin["hp"] += 30
            robin["def"] += 5
            robin["res"] += 5
            running = 0
        elif asset == "2":
            robin["str"] += 15
            robin["skl"] += 5
            robin["def"] += 5
            running = 0
        elif asset == "3":
            robin["mag"] += 15
            robin["spd"] += 5
            robin["res"] += 5
            running = 0
        elif asset == "4":
            robin["str"] += 15
            robin["str"] += 5
            robin["def"] += 5
            running = 0
        elif asset == "5":
            robin["spd"] += 15
            robin["skl"] += 5
            robin["lck"] += 5
            running = 0
        elif asset == "6":
            robin["lck"] += 15
            robin["str"] += 5
            robin["mag"] += 5
            running = 0
        elif asset == "7":
            robin["def"] += 15
            robin["lck"] += 5
            robin["res"] += 5
            running = 0
        elif asset == "8":
            robin["res"] += 15
            robin["spd"] += 5
            robin["mag"] += 5
            running = 0
        else:
            asset = input("please choose a number between 1 and 8: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
    
    flaw = input("choose robin's flaw: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
    running = 1
    while running == 1:
        if flaw == asset:
            flaw = input("asset and flaw cannot be the same: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
        elif flaw == "1":
            robin["hp"] -= 20
            robin["def"] -= 5
            robin["res"] -= 5
            running = 0
        elif flaw == "2":
            robin["str"] -= 10
            robin["skl"] -= 5
            robin["def"] -= 5
            running = 0
        elif flaw == "3":
            robin["mag"] -= 10
            robin["spd"] -= 5
            robin["res"] -= 5
            running = 0
        elif flaw == "4":
            robin["str"] -= 10
            robin["str"] -= 5
            robin["def"] -= 5
            running = 0
        elif flaw == "5":
            robin["spd"] -= 10
            robin["skl"] -= 5
            robin["lck"] -= 5
            running = 0
        elif flaw == "6":
            robin["lck"] -= 10
            robin["str"] -= 5
            robin["mag"] -= 5
            running = 0
        elif flaw == "7":
            robin["def"] -= 10
            robin["lck"] -= 5
            robin["res"] -= 5
            running = 0
        elif flaw == "8":
            robin["res"] -= 10
            robin["spd"] -= 5
            robin["mag"] -= 5
            running = 0
        else:
            flaw = input("please choose a number between 1 and 8: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")

RobinPrompt()

for stat in result:
    result[stat] = ((chrom[stat] + robin[stat] + lucina[stat]) / 3) + lord[stat]

for stat in result:
    print(stat + ": " + str(math.floor(result[stat])))

for stat in result:
    print(stat + ": " + str(math.floor(robin[stat])))