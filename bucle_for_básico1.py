#1 Básico: imprime todos los números enteros del 0 al 150.
print("Enteros 0 al 150")
for x in range(151):
    print(x)

# while loop version
print("Enteros 0 al 150 - while loop")

num = 0 
while num < 151:
    print(num)
    num += 1

#2 Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
print("Multiplos de Cinco")
for x in range(5, 1001, 5):
    print(x)

# while loop version
print("Multiplos de Cinco - while loop")
n = 5
while n < 1001:
    print(n)
    n += 5

#3 Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
#Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

print("Contando al estilo Dojo")
for c in range(1, 101):
    if c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

#4 Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

print("Whoa. Es un gran idiota!")
sum = 0 
for y in range(1, 500001, 2):
    sum += y
print(sum)

#5 Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
print("Cuenta regresiva de a 4")
for z in range(2018, 0, -4):
    print(z)

#6 Contador flexible: establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
#Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

print("Contador flexible")

lowNum = 2
highNum = 9
mult = 3
for f in range(lowNum, highNum + 1):
    if f % mult == 0:
        print(f)
