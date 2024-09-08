from claseCinta import Cinta_de_correr

def main():
    cintaDeCorrerUno = Cinta_de_correr("Bringeri", "RANDER 320", 120, "1.5 HP", 3, 22 )
    print(str(cintaDeCorrerUno))
    print("--------------------------- \n")
    
    cintaDeCorrerUno.iniciar_ejercicio(20, 30)
    cintaDeCorrerUno.iniciar_ejercicio(10, 20)
    cintaDeCorrerUno.iniciar_ejercicio(15, 40)
    
    print(f'Cantidad de Rutinas realizadas: {len(cintaDeCorrerUno)}')
    print(cintaDeCorrerUno.rutinas)
    print(f' Distancia total recorrida: {cintaDeCorrerUno.mostrar_distancia_recorrida_total()}')
    
    print("--------------------------- \n")
    cintaDeCorrerUno.reiniciar_valores()
    print(cintaDeCorrerUno.velocidad)
    print(cintaDeCorrerUno.tiempo)
    print(cintaDeCorrerUno.rutinas)

if __name__ == "__main__":
    main()