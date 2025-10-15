from math import exp

def CalculadoraConcentracaoPortadores(material: str, temperaturaKelvin: float, tipoDopagem: str = None, concentracaoDopante: float = None):
    '''
    Equação de ni = Km x T^3/2 x exp -Eg / 2 x k x T

    Km - Constante do material
    T - Temperatura
    Eg - Energia de Bandgap
    k - Constante de Boltzmann
    '''

    Km, Eg, ni = None, None, None
    k = 1.380649e-23 # J/K
    eV_to_J = 1.602176634e-19 # Conversão de eV para Joules
    T = temperaturaKelvin

    if material.lower() == "silicio":
        Km = 5.2e+15
        Eg = 1.12 * eV_to_J  # 1.12eV em Joules

    elif material.lower() == "germanio":
        Km = 1.66e+15
        Eg = 0.66 * eV_to_J  # 0.66eV em Joules

    else:
        raise ValueError("Material não suportado. Use 'silicio' ou 'germanio'.")

    ni = Km * (T ** 1.5) * exp(-Eg / (2 * k * T)) # elétrons/cm³

    if tipoDopagem and concentracaoDopante:
        if tipoDopagem.lower() == "n":
            n = concentracaoDopante
            p = ni ** 2 / n

        elif tipoDopagem.lower() == "p":
            p = concentracaoDopante
            n = ni ** 2 / p

        else:
            raise ValueError("Tipo de dopagem inválido. Use 'n' ou 'p'.")
        
        return ni, n, p
    
    return ni

def __main__():
    material = "germanio"
    temperatura = 300  # Kelvin
    tipoDopagem = "n"
    concentracaoDopante = 2e17  # cm^-3

    ni, n, p = CalculadoraConcentracaoPortadores(material, temperatura, tipoDopagem, concentracaoDopante)
    print(f"Material: {material}")
    print(f"Temperatura: {temperatura} K")
    print(f"Concentração intrínseca (ni): {ni:.2e} cm^-3")
    print(f"Concentração de elétrons (n): {n:.2e} cm^-3")
    print(f"Concentração de lacunas (p): {p:.2e} cm^-3")

if __name__ == "__main__":
    __main__()