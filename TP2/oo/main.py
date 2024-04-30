import clases
import front

def main():
     # default option centroid, bisector, MOM, SOM, LOM
    algo = clases.fuzzy_logic(250)
    algo.func_pertenencia()

    test = clases.pendulo(10, 0.001, 180, 0, 0,2,1,1)
     #t_max, dt, angulo_inicial, velocidad_inicial, posicion_carro, fuerza, masa_carro, masa_pendulo
    test.simular(algo)

    test.graficar()

    #front.graficar_pendulo(test.y, test.posicion_carro,test.x,test.f,test.velocidad_carro)

    

if __name__ == "__main__":
    main()