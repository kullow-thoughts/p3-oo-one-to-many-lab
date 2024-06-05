class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name,pet_type,owner="me"):
        self.name=name
        self.owner=owner
        self.pet_type=None
        self.set_pet_type(pet_type)
        self.all.append(self)
    
    def set_pet_type(self,pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception
        else:
            self.pet_type=pet_type

class Owner:
    def __init__(self, name):
        self.name=name

    def pets(self):
        return [pet for pet in Pet.all if self==pet.owner]
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner=self
        else:
            raise Exception
    def get_sorted_pets(self):
          return sorted(self.pets(), key=lambda pet: pet.name)