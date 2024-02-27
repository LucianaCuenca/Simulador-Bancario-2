class CuentaCorriente:
        ''''--------------
        #atributos
        -----------------'''
        saldo="1000"
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