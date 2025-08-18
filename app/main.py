class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)
    for i in range(len(people)):
        person_dict = people[i]
        person = person_list[i]
        if person_dict.get("wife") is not None:
            person.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband") is not None:
            person.husband = Person.people[person_dict["husband"]]
    return person_list
