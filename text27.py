foodNeed = set()
oneMaterial = input("Please enter one material of food that on your dinner list:")
while oneMaterial:
    foodNeed.add(oneMaterial)
    oneMaterial = input("Please enter one material of food that on your dinner list(enter Enter to quit):")
haveHad = set()
oneMaterial = input("Please enter one material of food that you have had:")
while oneMaterial:
    haveHad.add(oneMaterial)
    oneMaterial = input("Please enter one material of food that you have had(enter Enter to quit):")
canUse = haveHad & foodNeed
foodNeed = foodNeed - canUse
print("You need buy some material of food under the list:")
print(foodNeed)
