import random
simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

o = int(input('сколько символов должно быть в пароле?'))

pasvord = ''

for i in range(o):
    pasvord += random.choice(simvol)
    


print(pasvord)
