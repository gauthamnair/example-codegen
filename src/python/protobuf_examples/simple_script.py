from simple_example.v1.person_pb2 import Person
import networkx as nx


if __name__ == '__main__':
    p = Person()
    p.name = "Me"
    p.id = 3
    p.email = "me@example.com"
    print(p)
    print(f'Networkx version: {nx.__version__}')
