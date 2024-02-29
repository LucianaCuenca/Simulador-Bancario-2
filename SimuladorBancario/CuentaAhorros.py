class CuentaAhorros:
        ''''---------------
        #atributos
        -------------'''
        saldo="1000"
        interesMensual="0.6"
        '''--------------
        #metodos
        -----------------'''

        def ConsultarSaldo(self):
             return self.saldo
        
            
        def ConsignarValor(self):
            nSaldo = self.saldo + self.saldoConsignado
            self.saldo = nSaldo

        def CalcularInteresMensual(self):
            nSaldo = self.saldo * 0.6
            nSaldo = nSaldo + self.saldo
            self.saldo = nSaldo
            return nSaldo
        
        def DuplicarAhorro(self):
             self.saldo*2

             
        
          
 



                

        