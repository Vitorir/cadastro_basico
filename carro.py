class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, quantidade):
        self.velocidade += quantidade

    def frear(self, quantidade):
        if self.velocidade - quantidade >= 0:
            self.velocidade -= quantidade
        else:
            self.velocidade = 0

    def ligar(self):
        print(f"{self.marca} {self.modelo} ligou.")

    def desligar(self):
        print(f"{self.marca} {self.modelo} desligou.")

    def status(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")

# Exemplo de uso da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022, "Prata")

meu_carro.ligar()
meu_carro.acelerar(50)
meu_carro.status()
meu_carro.frear(20)
meu_carro.status()
meu_carro.desligar()
