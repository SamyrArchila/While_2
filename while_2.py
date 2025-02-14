print("--------------------------------------------------------------------")
AlturaInicial = float(input("Ingrese la altura inicial (AlturaInicial): "))
print("--------------------------------------------------------------------")

Rebotes = 0
AlturaActual = AlturaInicial


while AlturaActual >= AlturaInicial / 5:
    Rebotes += 1
    AlturaActual *= 0.9

print("----------------------------------------------------------------------------------------------------")
print(f"La pelota no alcanza a subir, la quinta parte de la altura inicial en el rebote número {Rebotes}.")
print("----------------------------------------------------------------------------------------------------")