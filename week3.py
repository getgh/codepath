# Session 1:
# Problem 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

# Problem 3: Catchphrase

def print_catchphrase(character):
    if character =='Pooh':
        print("Oh bother!")
    elif character =='Tigger':
        print("TTFN: Ta-ta for now!")
    elif character =='Eeyore':
        print("Thanks for noticing me.")
    elif character =='Christopher Robin':
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

# # Problem 5: Total Honey
def sum_honey(hunny_jars):
    c=0
    for x in hunny_jars:
        c+=x
    print(c)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)


# Problem 7: Poohsticks
def count_less_than(race_times, threshold):
    count = 0
    for i in race_times:
        if i < threshold :
            count += 1
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

# Problem 9: Pairs
def can_pair(item_quantities):
    for num in item_quantities:
        if num % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))
# Problem 11: T-I-Double Guh-ER
#Problem 11:
def tiggerfy(s):
    l = ['t', 'i', 'g', 'e', 'r']
    r = ""
    for i in s:
        if i.lower() not in l:
            r += i
        return r

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
