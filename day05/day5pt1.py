with open("day5/input5.txt") as f:
    lines = f.read()

rules, updates = lines.split("\n\n")

rules_dict = {}
for rule in rules.split("\n"):
    l, r = rule.strip().split("|")
    if int(l) not in rules_dict.keys():
        rules_dict[int(l)] = []
    rules_dict[int(l)].append(int(r))


total = 0
for update in updates.split("\n"):
    update = [int(x) for x in update.strip().split(",")]

    
    valid = True
    for item in update:
        if item not in rules_dict.keys():
            continue
        
        
        for item2 in rules_dict[item]:
            if item2 not in update:
                continue

            if update.index(item2) < update.index(item):
                valid = False
                break

        if not valid:
            break
        
    if valid:
        total += update[len(update) // 2]

print(total)

