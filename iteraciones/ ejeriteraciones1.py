import random
print("text")
moneda=input("ingrese la moneda")
cantidad=float(input("ingrese la cantidad de "+moneda+":"))
count=0
while count < 7:
        profit=random.uniform(-0.03,0.03)
        cantidad=cantidad+(cantidad*profit)
        count=count+1
        print("saldo de ",moneda,"el dia",count,"es de: %6.7f"%cantidad+".Ganancia de %6.2f"%(profit*100),"%")