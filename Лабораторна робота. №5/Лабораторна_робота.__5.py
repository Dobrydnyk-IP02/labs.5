n=int(input ("Введіть натуральне число: ")) # число, яке вводить користувач
p=n # змінна присвоєння введеного числа
x=0 # вираховування кількості цифр у двоїчному коді
res=0 # результат
c=int # змінна обчислення оберненого двійкового коду числа n
if n<0:
    print ("error") # число має бути натуральним
else:
    while p>1: # вираховування кількості цифр в двійковому коді
     x=x+1
     p=int(p/2)
 
    while n>0: #обчислення оберненого двійкового коду числа n
          c=n%2 
          n=int(n/2)
          res+=c*(2**x) #перевід у десяткову СЧ
          x=x-1
    print (res)