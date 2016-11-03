doors = [None] * 100
for hall in range(1,101):
    doors[hall-1] = "open"

for hall in range(1,101):
    for door in range(hall,101,hall):
        if doors[door-1] == "open":
            doors[door-1] = "close"
        else:
            doors[door-1] = "open"

def given(lista):
    OpenDoors = []
    for hall in range(len(lista)):
        if lista[hall] == "close":
            opened = str(hall+1)
            OpenDoors.append(opened)
    numbers = ','.join(OpenDoors)
    OpenDoorsText = "This doors are open: "
    print(OpenDoorsText+numbers)

print(given(doors))
