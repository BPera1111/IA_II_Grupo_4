import clases

def main():
     # default option centroid, bisector, MOM, SOM, LOM
    algo = clases.fuzzy_logic(100)
    algo.func_pertenencia()

    test = clases.pendulo(10, 0.001, -50, 0, 0,2,1,1)
    test.simular(algo)

    test.graficar()

    

if __name__ == "__main__":
    main()