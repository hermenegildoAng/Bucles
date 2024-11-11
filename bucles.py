'''
ciclo for en phyton
permite realizar una serie de instrucciones 
una cantidad determinada de veces

estructura
for i in [1...n]

range(fin)
    range(3)  [0,1,2]

range(inicio,fin,saltos o pasos)  
    range(2,9,2)  [2,4,6,8]
    
    
'''

n = int(input("Escriba un numero: "))

for x in range(1,11):
    r = n * x
    
    print(f" {n} X {x} = {r}")