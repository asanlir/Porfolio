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
    capit = input("¿Capitalización mensual o anual? (m/a) ").lower()

    return cap_ini, contrib, interes, anualidades, capit


def validar_capitalizacion(capit):
    """
    Valida la elección de capitalización.
    """
    if capit not in ["m", "a"]:
        print("Por favor, seleccione una opción válida")
        return False
    return True


def calc_int_simp(cap_ini, contrib, interes, anualidades):
    """
    Calcula el rendimiento con una capitalización anual
    """
    pass


def calc_int_comp(cap_ini, contrib, interes, anualidades):
    """
    Calcula el rendimiento con capitalización compuesta mensual.
    """
    pass


def main():
    pass


if __name__ == "__main__":
    main()


while True:
    respuesta = input("\n¿Desea realizar otra simulación? (s/n): \n")
    if respuesta.lower() == "s":
        main()
    else:
        break
