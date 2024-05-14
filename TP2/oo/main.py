import clases
import front
import threading
import multiprocessing



def main():
    pendulo = clases.fuzzy_logic(650,180,20,'pendulo')#fmax,pmax,vmax,tipo,defuzz; centroid/bisector/MOM/SOM/LOM default:centroid  
    pendulo.func_pertenencia()


    carrito = clases.fuzzy_logic(300,20,50,'carrito')
    carrito.func_pertenencia()


    test1 = clases.pendulo(5, 0.001, 45, 0, 0,2,1,1)
    #t_max, dt, angulo_inicial, velocidad_inicial, posicion_carro, fuerza, masa_carro, masa_pendulo
    test1.simular_pendulo(pendulo)
    # test1.graficar_en_hilo()
    

    test2=clases.pendulo(40,0.001,45,0,0,2,1,1)
    test2.simular_pendulo_carro(pendulo,carrito)


    multiprocessing.Process(target=test1.graficar,args=("Pendulo",)).start()

    multiprocessing.Process(
        target=front.graficar_pendulo, 
        args=(test1.y, test1.posicion_carro,test1.x,test1.f,test1.velocidad_carro,"Pendulo")
        ).start()


    multiprocessing.Process(target=test2.graficar,args=("Pendulo y Carrito",)).start()

    
    multiprocessing.Process(
        target=front.graficar_pendulo, 
        args=(test2.y, test2.posicion_carro,test2.x,test2.f,test2.velocidad_carro,"Pendulo y Carrito")
        ).start()
    

if __name__ == "__main__":
    main()