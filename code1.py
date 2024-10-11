import random

trap1 = open("Trap1.txt").read()
trap2 = open("Trap2.txt").read()
trs1 = open("Trs1.txt").read()
trs2 = open("Trs2.txt").read()
ent = open("ent.txt").read()
intro = open("intro.txt").read()
apple = open("apples.txt").read()
ext = open("ext.txt").read()


money = 100
hp = 100
ammo = 5
exit_game = False

def check(ag):
    global exit_game
    bah = ag.split("!!")[0]
    if bah == "YUMMM":
        heal()
        finance("-15")
    elif bah =="OUCH":
        damage("25")
    elif bah =="OHNO":
        shoot()
        finance("-25")
    elif bah=="YAY":
        finance("10")
        damage("10")
    elif bah=="WOO":
        finance("20")
        damage("-15")
    elif bah =="FINALLY":
        exit_game = True

def stats():
    print(f"Your stats are:\nMoney: {money}")
    print(f"Health points: {hp}")
    print(f"Taser ammo: {ammo}")


L1, L2, L3, L4 = [], [], [], []
room_set = [trap1, trap2, trs1, trs2, apple]

for i in range(3):
    L1.append(random.choice(room_set))
    L2.append(random.choice(room_set))
    L3.append(random.choice(room_set))
    L4.append(random.choice(room_set))

a = random.choice(range(3))
L1[2] = ent  
L4[a] = ext  

Play = True
position = ["1", "2"]  # 1th , 2th starting pos


def pos():
    row = int(position[0]) - 1 
    col = int(position[1]) - 1
    bab = [L1, L2, L3, L4][row][col]
    return bab

def damage(dmg):
    global hp
    hp -= int(dmg)
    print(f"Damage taken: {dmg}, HP remaining: {hp}")
    if hp <= 0:
        global Play
        Play = False

def shoot():
    global ammo
    if ammo > 0:
        ammo -= 1
        print(f"Ammo used. Remaining ammo: {ammo}")
    else:
        print("You have run out of ammo. Lose health.")
        global hp
        hp -= 10

def heal():
    global hp
    hp += 25
    print(f"Health increased. Current HP: {hp}")

def reload(a):
    global ammo
    ammo += int(a)
    print(f"Ammo reloaded. Current ammo: {ammo}")

def finance(a):
    global money
    money += int(a)
    
    if money < 0:
        print("You have no money. Lose health.")
        global hp
        hp -= 10
           

print(intro)
stats()


while hp > 0 and not exit_game:
    m = input("Move: up(U), down(D), left(L), right(R): ").upper()

    if m == "U":
        if position[0] != "4":  # Move up
            position[0] = str(int(position[0]) + 1)
        else:
            position[0] = "1"  # Wrap around to row 1
        print(pos())
        check(pos())
        stats()

    elif m == "D":
        if position[0] != "1":  # Move down
            position[0] = str(int(position[0]) - 1)
        else:
            position[0] = "4"  
        print(pos())
        check(pos())
        stats()

    elif m == "R":
        if position[1] != "3":  
            position[1] = str(int(position[1]) + 1)
        else:
            position[1] = "1"  
        print(pos())
        check(pos())
        stats()

    elif m == "L":
        if position[1] != "1": 
            position[1] = str(int(position[1]) - 1)
        else:
            position[1] = "3" 
        print(pos())
        check(pos())
        stats()

    else:
        print("Invalid move. Please use U, D, L, or R.")

# End game 
if hp <= 0:
    print("You have died.")
    stats()
elif exit_game:
    print("You have exited the mansion.")
    stats()

#trap1.close()
#trap2.close()
#trs1.close()
#trs1.close()
#apple.close()
#ent.close()
#ext.close()
#intro.close()
# project made by Kunal and Vandith.
