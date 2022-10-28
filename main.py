from Classes.Triangle import Triangle
from Classes.Square import Square

def main(status):
    print(status, end='\n\n')

    Tr0 = Triangle(10,6,9)
    print(Tr0)
    del Tr0
    print()

    Sq0 = Square(10, 15)
    print(Sq0)
    del Sq0

if __name__ == '__main__':
    main('Running...')


