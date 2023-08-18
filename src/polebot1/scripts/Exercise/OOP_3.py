# object oriented programming 
# template = class

class polebot : #template
    #class variabel
    jumlah = 0
    
    def __init__(self,inputName,inputPower,inputStrenght):
        #instance variabel hanya dimiliki oleh polebot aja liat deket class
        self.name = inputName
        self.power = inputPower
        self.strenght = inputStrenght
        polebot.jumlah  += 1
        print("membuat polebot dengan nama " +inputName)


polebot1 = polebot("aku", 200, 100)
print(polebot.jumlah)
polebot2 = polebot("wow", 1000, 10000)
print(polebot.jumlah)
polebot3 = polebot("sangat", 10, 100)
print(polebot.jumlah)


# print(polebot1. __dict__)
# print(polebot2. __dict__)
# print(polebot3. __dict__)
# print(polebot. __dict__)
