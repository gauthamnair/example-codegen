from simple_example.v1.person_pb2 import Person

if __name__ == '__main__':
    p = Person()
    p.name = "Me"
    p.id = 3
    p.email = "me@example.com"
    print(p)
