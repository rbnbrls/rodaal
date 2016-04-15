salaris = 2550
invoer = int(input("Wat is je salaris?"))
rodaal = invoer/salaris
if rodaal > 1:
    rodaal = (rodaal - 1)*100
    print("Gefeliciteerd, je salaris is",round(float(rodaal), 2),"% boven rodaal.")
else:
    rodaal = (1 - rodaal)*100
    print("Helaas, je salaris ligt",round(float(rodaal), 2),"% onder rodaal.")