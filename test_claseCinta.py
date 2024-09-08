from claseCinta import Cinta_de_correr

    
    







        



def test_cinta_de_correr():
    miCinta = Cinta_de_correr("su marca", "su modelo", 120, 22)
    miCinta.iniciar_Ejercicio(10, 30)
    miCinta.iniciar_Ejercicio(20, 15)
    miCinta.iniciar_Ejercicio(15, 40)
    assert miCinta.mostrar_distancia_recorrida_total() == 20