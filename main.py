from pelicula import Pelicula

if __name__ == "__main__":

    pelicula1 = Pelicula(8975, "Talk To Me", 95, "Michael Philippou", False)
    pelicula2 = Pelicula(2856, "Five Nights at Freddy's", 110, "Emma Tammi", True)
    pelicula3 = Pelicula(8975, "Super Mario Bros", 92, "Aaron Horvath", False)
    
    print(pelicula1)
    print(pelicula2)
    print(pelicula3)

    print(pelicula1.prestar())
    print(pelicula2.prestar())
    print(pelicula3.devolver())

    print(pelicula1.costo_reproduccion(100))
    print(pelicula2.costo_reproduccion(100))
    print(pelicula3.costo_reproduccion(100))
    
    print("¿pelicula1 y pelicula2 son iguales?", pelicula1 == pelicula2)
    print("¿pelicula1 y pelicula3 son iguales?", pelicula1 == pelicula3)