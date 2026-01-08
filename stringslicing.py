my_str = 'Hello World'

print(my_str[5]) # [ ]
print(my_str[10]) # d

# NOTE =  STRING SLICING LETS YOU EXTRACT APORTION OF STRING OR WORK WITH ONLY A SPECIFIC PART OF IT BY USE OF START AND STOP DEVIDED BY COLON : BTW THEM

# STRING SLISING BY USE OF {:} 
print(my_str[1:4]) # ell
print(my_str[6:10]) # worl
print(my_str[0:3]) # Hel

#OMITING THE START AND PYTHON WILL DEFAULT TO ZERO
print(my_str[:7]) # Hello w
print(my_str[:5]) # Hello

#OMMITTING THE STOP ,IT WILL WRITE EVERY THING TO THE END OF THE STRING
print(my_str[8:]) # rld
print(my_str[3:]) # lo world
print(my_str[5:]) #  world
print(my_str[0:]) # Hello world

print(my_str[8:])
print(my_str)

#OMMITTING BOTH START AND STOP IT WILL EXTRACT THE WHOLE STRING
print(my_str[:]) #Hello world

#USING START , STOP AND STEP (PARAMETER)

print(my_str[0:11:2])# Hlowrd
print(my_str[0:11:3])#Hlwl

#USING THE REVERSE (PARAMETER)
print (my_str[::-1]) # dlrow olleHS