from calc_concentracao_portadores import CalculadoraConcentracaoPortadores

def CalcularCorrenteDeriva(tensao: float, comprimento: float, largura: float, altura: float, temperaturaKelvin: float, tipoDopagem: str, concentracaoDopagem: float):
    '''
        Fórmula para calcular corrente de deriva:
            I = -v x W x h x n x q
                v: vetor velocidade (elétrons e lacunas)
                W: largura da barra de silício
                h: altura da barra de silício
                n: concentração de elétrons
                q: carga fundamental do elétron
            
            I = Jtotal x W x h

            Jtotal = q x (un x n + up x p) x E
                un: mobilidade dos elétrons no silício
                up: mobilidade das lacunas no silício
                p: concentração de lacunas
                E: campo elétrico

            E = V / L
                V: tensao
                L: comprimento da barra de silício
    '''

    V = tensao
    L, W, h = comprimento, largura, altura
    vn, vp = None, None
    I, Jtotal = None, None

    q = 1.6e-19
    un = 1350
    up = 480
    
    E = V / L # campo elétrico

    ni, n, p = CalculadoraConcentracaoPortadores("silicio", temperaturaKelvin, tipoDopagem, concentracaoDopagem)

    vn = -un * E
    vp = up * E

    Jtotal = q * (un * n + up * p) * E
    I = Jtotal * W * h

    return E, n, p, vn, vp, Jtotal, I


