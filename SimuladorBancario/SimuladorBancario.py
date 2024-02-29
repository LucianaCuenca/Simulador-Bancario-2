from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente

class SimuladorBancario:
        ''''-----------------
        #atributos
        --------------'''
        cedula=""
        nombre=""
        mesActual=""

        ''''----------------------
        #Asociaciones
        --------------------------'''
        saldoCorriente = CuentaCorriente
        cambiarCuentas = CuentaAhorros , CuentaCorriente

        '''-----------------
        #metodos
        --------------------'''
        
        def ConsultarNombre(self):
         return self.nombre
        
        def ConsultarCedula(self):
            return self.cedula
         
        def ConsutarMesActual(self):
            return self.mesActual
        
        def ConsultarSaldoCorriente(self):
            return "Tu saldo en cuenta corriente es "+self.saldoCorriente.ConsultarSaldo()
      
            
       
        
    