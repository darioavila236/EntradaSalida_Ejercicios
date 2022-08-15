import pickle

def main():
    f = open('datos.bin','rb')
    vehiculo = pickle.load(f)
    f.close()
    print(vehiculo)
class Vehiculo:
    nombre = " "
    año = 0

    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año


if __name__ == "__main__":
    main()

