# object oriented programming 
# template = class

class polebot : #template
    pass


move1 = polebot() #object
move2 = polebot()

move1.gerak = "kanan"
move1.panjang = 100

move2.gerak = "kiri"
move2.panjang = 100


print(move1)
print(move1.__dict__)
print(move1.gerak)