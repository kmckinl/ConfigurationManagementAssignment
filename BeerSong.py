def Main():
    Ninety_Nine_Bottles_of_Beer()
    
def Ninety_Nine_Bottles_of_Beer():
    for x in range(0, 99):
        y = 99 - x
        z = y - 1
        if (y > 1):
            print(str(y) + " bottles of beer on the wall, " + str(y)  +" bottles of beer")
            print("take one down, pass it around, " + str(z)  + " bottles of beer on the wall")
        else:
            print(str(y) + " bottles of beer on the wall, " + str(y)  +" bottles of beer")
            print("take one down, pass it around, no more bottles of beer on the wall")
            
Main()  
    
