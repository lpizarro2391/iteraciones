horasTrabajadas = int(input("¿Cuántas horas se trabajaron en la semana? "))
pagoHora=10
if horasTrabajadas <= 40:
   totalCobro = pagoHora*horasTrabajadas
else:
   sobretiempo = horasTrabajadas - 40
   totalCobro = pagoHora*40 + 1.5*pagoHora*sobretiempo
print("Total a cobrar: "+str(totalCobro))
