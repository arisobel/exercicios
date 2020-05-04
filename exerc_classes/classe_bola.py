class Bola:
    """
    implementa a classe bola
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
    """
    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self.material = material
        self.circunferencia = circunferencia
    def troca_cor(self, nova_cor):
        self._cor = nova_cor
    def mostra_cor(self):
        print(f"A cor da bola é {self._cor}")


