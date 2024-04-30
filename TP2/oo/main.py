import clases
import front

def main():
    pendulo = clases.fuzzy_logic(250,180,20,'pendulo')#fmax,pmax,vmax,tipo,defuzz; centroid/bisector/MOM/SOM/LOM default:centroid  
    print("1")
    pendulo.func_pertenencia()
    print("2")


    carrito = clases.fuzzy_logic(250,100,50,'carrito')
    carrito.func_pertenencia()


    test = clases.pendulo(10, 0.001, 180, 0, 0,2,1,1)
    #t_max, dt, angulo_inicial, velocidad_inicial, posicion_carro, fuerza, masa_carro, masa_pendulo
    print("3")
    test.simular(pendulo,carrito)
    print("4")

    #test.graficar()

    front.graficar_pendulo(test.y, test.posicion_carro,test.x,test.f,test.velocidad_carro)

    

if __name__ == "__main__":
    main()