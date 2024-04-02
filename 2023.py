a = 2023
b = 2024
c = 2025

print("Ver cada cuanto aparece la secuencia 2023-2024-2025")
print("----------------------------------------------------")

i = 4
contador = 0
while contador < 11:
    if a == 2023 and b == 2024 and c == 2025:
        contador += 1
        print("a=2023, b=2024 y c=2025. Vez:", contador, "   i:", i)

    r = (a + b + c) % 10000
    if i < 7 or i == 50:
        print("Chequeo de correcto calculo: i:", i, "   Resultado:", r)

    a, b, c = b, c, r
    i += 1

print("\nRespuesta: La secuencia 2003-2004-2005 empieza cada 124000 procesos\n")

print("Ahora realizo el proceso para saber los 4 ultimos dígitos para el momento 2023202320232023")
print("Para eso calculo cuantas veces entra 2023202320232023 en 124000 y me posiciono")
print("en la ultima vez anterior al numero con datos conocidos")
print("(cuando a es 2023 b es 2024 y c es 2025), y cuento y calculo desde ahi.")
print("------------------------------------------------------------------------------------------")

veces = int(2023202320232023 / 124000)

# Me posiciono
i = veces * 124000 + 4
# Pongo a, b y c en las cifras que sé que poseen porque ya lo demostré
a = 2023
b = 2024
c = 2025

while i <= 2023202320232023:
    r = (a + b + c) % 10000
    a, b, c = b, c, r
    i += 1

print("Respuesta: para la vez 2023202320232023 se imprimirá:", r)
print(" --- * --- ")
