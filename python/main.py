from proto import person_pb2 as person

p = person.Person()

p.age = 1
person.first_name = "bob"
person.last_name = "smith"

print(p)