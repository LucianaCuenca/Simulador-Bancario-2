from Fecha import Fecha

class Empleado: 
    #aqui va el codigo

    '''------------------
    #Atributos
    ------------------'''

    nombre=''
    apellido=''
    '''-----------------
    # 1 = Masculino y 2 = Femenino
    -----------------'''
    sexo=0
    salario=0

    ''''----------------------
    #asociaciones
    ---------------------'''

    fechaNacimiento=Fecha()
    fechaIngreso=Fecha()
    
    '''----------------------------
    # Metodos
    ----------------------------'''

    def CambiarEmpleado(self, nNombre, nApellido, nSexo, NsSalario):  
           #aqui va el codigo del nuevo empleado
         return None            
        
      
    def ConsultarNombre(self):
         return self.nombre
    

    def ConsultarApellido(self):
          return self.apellido
    

    def ConsultarNombreCompleto(self):
          return self.nombre +" "+ self.apellido
    
    
    def CambiarSalario(self, nSalario):
        #Aquí va el codigo
        self.salario = nSalario
        return  'su nuevo salario es: '+self.salario       
    
    def ConsultarSalario(self):
        #Aquí va el codigo
        return self.salario
    
    def AumentoSalario(self):
        #Aquí va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return  'su nuevo salario es: '+self.salario
    
    def DuplicarSalario(self):
        # aqui va el codigo
        # forma 1
        # self.salario = self.salario*2
        # forma 2
        self.salario*= 2
        
    def CalcularSalarioAnual(self):
        #aqui va el codigo
        salarioAnual = self.salario*12
        return salarioAnual
        #forma 1
        #forma 2
        # return self.salario*12
    
    def ConsultarDiaCumpleaños(self):
        return "El dia de su cumpleaños es "+self.fechaNacimiento.ConsultarDia()
  
