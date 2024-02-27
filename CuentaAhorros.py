class CuentaAhorros:
        ''''---------------
        #atributos
        -------------'''
        saldo=""
        interesMensual="0.6"
        saldoConsignado=""
        saldoRetirado=""
        '''--------------
        #metodos
        -----------------'''
        def saldoConsignado(self):
           return self.saldoConsignado
            
        def saldoRetirado(self):
            return self.saldoRetirado
            
        def ConsignarValor(self):
            nSaldo = self.saldo + self.saldoConsignado
            self.saldo = nSaldo

        def retirarValor(self):
            nSaldo = self.saldo - self.saldoRetirado
            self.saldo = nSaldo
        def interesMensual(self):
           nSaldo = self.saldo * 0.6
           nSaldo = nSaldo + self.saldo
           self.saldo = nSaldo
                

            