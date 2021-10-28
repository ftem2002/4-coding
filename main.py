fridge = [ "egg" , "milk" , "juice" , "tomato" , "yogurt" , "pepper" ]
items  =input("enter the item :")
if items in fridge :
    print ("is found")
else :
    print("-1")

print (30*("_"))

# problem 1

fridge = ["flour" , "egg" , "salt" , "cheese" , "tomato paste"]
igredients = input("enter your ingredients :")

if igredients in fridge :
    print("true")
else :
    print("false")
print (30*("_"))

# problem 2


fridge = ["tomato" , "egg" , "cucumber" , "batato"]

tomato = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] ,
batato = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] ,
cucumber = [ 1 , 2 , 3 , 4 ] ,
eggs = [ 1 , 2 , 3 ]


ingredients = (int(input("enter your amount of egg : "))+ int(input("enter your amount of tomato: "))+ int(input("enter your amount of batato: "))+ int(input(" enter your amount of cucuber :")))


if ingredients in fridge == "":
    print (" you can")
else :
    print (" you cant")


# problem 3

fridge = ["tomato" , "egg" , "cucumber" , "batato"]

fridge.remove(fridge[3])
fridge.insert(3,["onions"])
print(fridge)