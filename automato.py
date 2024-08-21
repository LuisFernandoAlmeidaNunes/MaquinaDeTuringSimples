E = -1
D = 1
LIDO = 0
MOVIMENTO = 2
aceita = True

class Transicao:
    def __init__(self, lido, escreve, movimento, estado_novo):
        self.lido = lido
        self.escreve = escreve
        self.movimento = movimento
        self.estado_novo = estado_novo

    def __repr__(self):
        return (f"            Transicao(lido='{self.lido}', escreve='{self.escreve}', "
                f"movimento={self.movimento}, estado_novo={self.estado_novo})")

class Estado:
    def __init__(self):
        self.transicoes = []

    def __repr__(self):
        transicoes_repr = '\n'.join(repr(t) for t in self.transicoes)
        return f" transicoes=[\n{transicoes_repr}\n        ]"

class Automato:
    def __init__(self, inicial):
        self.inicial = inicial
        self.final = []
        self.estados = []

    def __repr__(self):
        estados_repr = '\n'.join(f"        q{i} ({estado})" for i, estado in enumerate(self.estados))
        return (f"Automato \n"
                f"    inicial={self.inicial},\n"
                f"    final={self.final},\n"
                f"    estados=[\n{estados_repr}\n    ]\n")

def faz_transicao(lido, transicoes, fita, pos):
    for transicao in transicoes:
        if lido == transicao["lido"]:
            movimento(lido, fita, pos, transicao["movimento"])

def movimento(escrito, fita, pos, movimento):
    fita[pos] = escrito
    return fita, (pos + movimento)

def cria_estado(automato, transicoes):
    q = Estado()
    q.transicoes = transicoes
    automato.estados.append(q)
    return automato

def cria_transicao(transicoes, lido, escrito, movimento, estado_novo):
    transicao = Transicao(lido, escrito, movimento, estado_novo)
    transicoes.append(transicao)
    return transicoes

if __name__ == "__main__":
    # Lista de cadeias
    strings = ['abc', 'aabcc', 'aabbc']

    # Inicializando autômato
    automato = Automato(0)
    automato.final.append(0)

    transicoes = []

    # Criando q0
    transicoes = cria_transicao(transicoes, "a", "F", D, 1)

    automato = cria_estado(automato, transicoes)

    print(automato.estados[0].transicoes)
    print(automato)
