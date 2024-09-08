class Cinta_de_correr:
    def __init__(self, marca, modelo, peso_maximo_soportado, motor, niveles_de_inclinacion, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__peso_maximo_soportado = peso_maximo_soportado
        self.__motor = motor
        self.__niveles_de_inclinacion = niveles_de_inclinacion
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad = 0
        self.__tiempo = 0
        self.__rutinas = []
    
    def __str__(self):
        return f'Marca: {self.__marca} \n Modelo: {self.__modelo} \n Motor: {self.__motor} \n Peso máximo soportado: {self.__peso_maximo_soportado} \n velocidad Máxima: {self.__velocidad_maxima} \n Niveles de Inclinación: {self.__niveles_de_inclinacion}'
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def tiempo(self):
        return self.__tiempo
    
    @property
    def rutinas(self):
        return self.__rutinas
    
    @velocidad.setter
    def velocidad(self, velocidad):
        if(velocidad > 0 and velocidad <= self.__velocidad_maxima):
            self.__velocidad = velocidad
        else:
            print("VELOCIDAD NO SOPORTADA")
            self.__velocidad = None    
        
    @tiempo.setter
    def tiempo(self, tiempo):
        if(tiempo > 0):
            self.__tiempo = tiempo
        else:
            print("TIEMPO NO SOPORTADO")
            self.__tiempo = None
    
    @rutinas.setter
    def rutinas(self, rutina):
        self.__rutinas.append(rutina)
        
    def __len__(self):
        return len(self.__rutinas)
    
    def iniciar_ejercicio(self, velocidad, tiempo):
        self.velocidad = velocidad
        self.tiempo = tiempo
        rutina = {
            "velocidad" : self.velocidad,
            "tiempo" : self.tiempo
        }
        self.rutinas = rutina
    
    def mostrar_distancia_recorrida_total(self):
        try:
            distancia_total = 0
    
            for rutina in self.rutinas:
                horas = rutina['tiempo'] / 60
                distancia = rutina['velocidad'] * horas
                distancia_total += distancia
    
            return round(distancia_total, 1)
        except Exception as e:
            print("Ocurrio un error", e)
            
    def reiniciar_valores(self):
        self.__velocidad = 0
        self.__tiempo = 0
        self.__rutinas = []
        
        

