def RobinPrompt(robin):
    asset = input("choose robin's asset: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
    running = True
    while running:
        if asset == "1":
            robin["hp"] += 30
            robin["def"] += 5
            robin["res"] += 5
            running = False
        elif asset == "2":
            robin["str"] += 15
            robin["skl"] += 5
            robin["def"] += 5
            running = False
        elif asset == "3":
            robin["mag"] += 15
            robin["spd"] += 5
            robin["res"] += 5
            running = False
        elif asset == "4":
            robin["skl"] += 15
            robin["str"] += 5
            robin["def"] += 5
            running = False
        elif asset == "5":
            robin["spd"] += 15
            robin["skl"] += 5
            robin["lck"] += 5
            running = False
        elif asset == "6":
            robin["lck"] += 15
            robin["str"] += 5
            robin["mag"] += 5
            running = False
        elif asset == "7":
            robin["def"] += 15
            robin["lck"] += 5
            robin["res"] += 5
            running = False
        elif asset == "8":
            robin["res"] += 15
            robin["spd"] += 5
            robin["mag"] += 5
            running = False
        else:
            asset = input("please choose a number between 1 and 8: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
    
    flaw = input("choose robin's flaw: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
    running = True
    while running:
        if flaw == asset:
            flaw = input("asset and flaw cannot be the same: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
        elif flaw == "1":
            robin["hp"] -= 20
            robin["def"] -= 5
            robin["res"] -= 5
            running = False
        elif flaw == "2":
            robin["str"] -= 10
            robin["skl"] -= 5
            robin["def"] -= 5
            running = False
        elif flaw == "3":
            robin["mag"] -= 10
            robin["spd"] -= 5
            robin["res"] -= 5
            running = False
        elif flaw == "4":
            robin["skl"] -= 10
            robin["str"] -= 5
            robin["def"] -= 5
            running = False
        elif flaw == "5":
            robin["spd"] -= 10
            robin["skl"] -= 5
            robin["lck"] -= 5
            running = False
        elif flaw == "6":
            robin["lck"] -= 10
            robin["str"] -= 5
            robin["mag"] -= 5
            running = False
        elif flaw == "7":
            robin["def"] -= 10
            robin["lck"] -= 5
            robin["res"] -= 5
            running = False
        elif flaw == "8":
            robin["res"] -= 10
            robin["spd"] -= 5
            robin["mag"] -= 5
            running = False
        else:
            flaw = input("please choose a number between 1 and 8: | 1: HP |  2: STR | 3: MAG | 4: SKL | 5: SPD | 6: LCK | 7: DEF | 8: RES |\n")
    return robin