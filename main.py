import child_growth_calc

print("\n----------------------------------------\n")
action = input("What would you like to do: | 1: child unit growth rates | 2: exit\n\n")
print("\n----------------------------------------\n")
running = True
while running:
    if action == "1":
        child_growth_calc.ChildPrompt()
        action = input("What would you like to do: | 1: child unit growth rates | 2: exit |\n\n")
        print("\n----------------------------------------\n")
    elif action == "2":
        running = False
    else:
        action = input("What would you like to do: | 1: child unit growth rates | 2: exit |\n\n")
        print("\n----------------------------------------\n")