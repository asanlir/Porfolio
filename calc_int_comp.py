"""
Calcula el crecimiento de una inversión durante un período de tiempo en base al capital inicial,
contribución periódica, tipo de interés y número de años.
"""

def obtener_datos_usuario():
    """
    Obtiene los datos del usuario para realizar el cálculo.
    """
    cap_ini = int(input("Indique su capital inicial: "))
    contrib = int(input("Indique su aportación mensual: "))
    interes = float(input("Indique el interés del depósito (%): ")) / 100
    anualidades = int(input("¿Cuántos años quiere simular?: "))
    capit = ""
    while True:
        capit = input("¿Capitalización mensual o anual? (m/a) ").lower()
        if validar_capitalizacion(capit):
            break

    return cap_ini, contrib, interes, anualidades, capit


def validar_capitalizacion(capit):
    """
    Valida la elección de capitalización.
    """
    if capit not in ["m", "a"]:
        print("Por favor, seleccione una opción válida ('m' para mensual o 'a' para anual).")
        return False
    return True


def calc_int_simp(cap_ini, contrib, interes, anualidades):
    """
    Calcula el rendimiento con una capitalización anual
    """
    contrib_anual = contrib * 12
    cap = cap_ini + contrib_anual # Se suma la aportación inicial y la aportación del primer año
    total_aportado = cap_ini + contrib_anual
    total_beneficios = 0

    print("\n")

    for i in range(anualidades):
        print(f"Capital base del año {i+1}: {cap:.2f}")

        # Calcular los intereses después de la aportación anual
        interes_ganado = cap * interes
        cap += interes_ganado
        total_beneficios += interes_ganado

        print(f"Interés ganado en el año {i+1}: {interes_ganado:.2f}")
        print(f"Capital después de intereses del año {i+1}: {cap:.2f}\n")

        # Añadir la aportación anual para el siguiente año, excepto en el último año
        if i < anualidades - 1:
            cap += contrib
            total_aportado += contrib

    print(f"Total aportado: {total_aportado:.2f}")
    print(f"Total beneficios generados por intereses: {total_beneficios:.2f}")
    print(f"Media de interés anual: {total_beneficios/anualidades:.2f}")
    print(f"Capital total después de {anualidades} años: {cap:.2f}")


def calc_int_comp(cap_ini, contrib, interes, anualidades):
    """
    Calcula el rendimiento con capitalización compuesta mensual.
    """
    cap = cap_ini
    total_aportado = cap_ini  # Incluye el capital inicial
    total_beneficios = 0

    print("\n")

    # Realizamos el ciclo mes a mes, pero solo imprimimos resultados al final de cada año
    for mes in range(anualidades * 12):
        # Calcula los intereses después de la aportación mensual
        interes_ganado = cap * interes / 12  # Interés mensual
        cap += interes_ganado + contrib  # Suma interés y contribución mensual
        total_aportado += contrib  # Aumenta el total aportado
        total_beneficios += interes_ganado  # Suma el interés ganado

        # Al final de cada año (cuando mes + 1 es múltiplo de 12), mostramos resultados
        if (mes + 1) % 12 == 0:
            year = (mes + 1) // 12
            print(f"Año {year}: ")
            print(f"  Total aportado: {total_aportado:.2f}")
            print(f"  Intereses generados hasta ahora: {total_beneficios:.2f}")
            print(f"  Capital total al final del año {year}: {cap:.2f}")
            print()

    # Resumen final
    print(f"Resumen final después de {anualidades} años:")
    print(f"Total aportado: {total_aportado:.2f}")
    print(f"Total beneficios generados por intereses: {total_beneficios:.2f}")
    print(f"Media de interés anual: {total_beneficios / anualidades:.2f}")
    print(f"Capital total después de {anualidades} años: {cap:.2f}")


def main():
    cap_ini, contrib, interes, anualidades, capit = obtener_datos_usuario()

    if not validar_capitalizacion(capit):
        return
    elif capit == "a":
        calc_int_simp(cap_ini, contrib, interes, anualidades)
    else:
        calc_int_comp(cap_ini, contrib, interes, anualidades)


if __name__ == "__main__":
    main()


while True:
    respuesta = input("\n¿Desea realizar otra simulación? (s/n): \n")
    if respuesta.lower() == "s":
        main()
    else:
        break
