from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente

class SimuladorBancario:
   ''''-----------------
   #atributos
   --------------'''
   cedula=''
   nombre=''
   mesActual=''
   '''---------------------
   # 1= VIP  2= Platino  3= Normal
   -----------------------'''

   tipoDeCliente=''

   ''''----------------------
   #Asociaciones
   --------------------------'''
   saldoCorriente = CuentaCorriente
   cambiarCuentas = CuentaAhorros , CuentaCorriente

   '''-----------------
   #metodos
   --------------------'''

   def __init__(self, nombre, cedula, mesActual, tipoDeCliente):
        self.nombre = nombre
        self.cedula = cedula
        self.mesActuals = mesActual
        self.tipoDeCliente = tipoDeCliente
   
       
        
   def ConsultarNombre(self):
      return self.nombre
        
   def ConsultarCedula(self):
       return self.cedula
         
   def ConsutarMesActual(self):
       return self.mesActual
   
   def ConsultarTipoDeCliente(self):
        return self.tipoDeCliente
        
   def ConsultarSaldoCorriente(self):
        return "Tu saldo en cuenta corriente es "+self.saldoCorriente.ConsultarSaldo()
      
            
   def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
   def CalcularSaldoTotal(self):
        # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()

        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
   def PasarAhorrosACorriente(self):
        # forma1
         self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
         self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        #saldoAhorros = self.ahorros.ConsultarSaldo()
        #self.corriente.saldo += saldoAhorros
        #self.ahorros.saldo = 0
        
   def ConsultarSaldoCorriente(self):
        return "Tu saldo es: "+self.corriente.ConsultarSaldo()
    
   def DuplicarAhorro(self):
        #forma 1
        self.ahorros.ConsignarMonto(self.ahorros.ConsultarSaldo())
        
        # # Forma 2
        # self.ahorros.saldo *= 2
    
   def RetirarTodo(self):
        total = self.CalcularSaldoTotal()
        self.corriente.RetirarMonto(self.corriente.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        return "Retiraste total: "+total   

   def cambiarTipoDeCliente(self, nuevoTipo):
        self.tipoDeCliente = nuevoTipo 
        return nuevoTipo

   def Retirarv(self):
        total = self.CalcularSaldoTotal()
        self.corriente.RetirarMonto(self.corriente.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        return "Retiraste total: "+total 

    