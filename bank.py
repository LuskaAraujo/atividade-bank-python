class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.saques_diarios = 0

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def saque(self, valor):
        if self.saques_diarios < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques_diarios += 1
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        elif self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            print("Limite diário de saques atingido ou valor de saque excede o permitido.")

    def extrato(self):
        print(f"Saldo atual: R${self.saldo}")


# Exemplo de uso:
conta = ContaBancaria(1000)  # Inicializa a conta com um saldo de R$ 1000

# Realiza algumas operações
conta.deposito(500)
conta.saque(200)
conta.saque(300)
conta.saque(400)
conta.saque(1000)  # Isso não será permitido devido ao valor do saque
conta.extrato()
