from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    return Person(full_name=faker_en.name(),
                  email=faker_en.email(),
                  current_address=faker_en.address().replace('\n', ' '),
                  permanent_address=faker_en.address().replace('\n', ' '))


