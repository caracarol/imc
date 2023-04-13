import os

altura = float(input("Informe sua altura (em metros): "))
peso = float(input("Informe seu peso (em Kg): "))

if altura.is_integer():
    altura = altura / 100
 
imc = peso / (altura**2)
 
print("Seu índice de massa corporal é: %.4f" % imc)
 
if imc < 16:
    print("Cuidado, você está muito abaixo do peso!")
elif imc < 18.5:
	print("Você está abaixo do peso.")
elif imc < 25:
	print("Você está saudável!")
elif imc < 30:
    print("Você está acima do peso.")
elif imc < 35:
    print("Você está muito acima do peso!")
else:
    print("Tome cuidado! Você está severamente acima do peso!")

os.system("pause")