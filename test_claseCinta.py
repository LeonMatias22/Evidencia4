from claseCinta import Cinta_de_correr

    
    







        



def test_cinta_de_correr():
    miCinta = Cinta_de_correr("su marca", "su modelo", 120, "1.5 HP", 3, 22)
    miCinta.iniciar_ejercicio(10, 30)
    miCinta.iniciar_ejercicio(20, 15)
    miCinta.iniciar_ejercicio(15, 40)
    assert miCinta.mostrar_distancia_recorrida_total() == 20