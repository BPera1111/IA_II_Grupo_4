import clases
import front

def main():
    pendulo = clases.fuzzy_logic(1000,180,20,'pendulo')#fmax,pmax,vmax,tipo,defuzz; centroid/bisector/MOM/SOM/LOM default:centroid  
    pendulo.func_pertenencia()


    carrito = clases.fuzzy_logic(1000,100,50,'carrito')
    carrito.func_pertenencia()


    test = clases.pendulo(10, 0.001, 45, 0, 0,2,1,1)
    #t_max, dt, angulo_inicial, velocidad_inicial, posicion_carro, fuerza, masa_carro, masa_pendulo
    test.simular(pendulo,carrito)
    test.graficar()

    front.graficar_pendulo(test.y, test.posicion_carro,test.x,test.f,test.velocidad_carro)

    

if __name__ == "__main__":
    main()