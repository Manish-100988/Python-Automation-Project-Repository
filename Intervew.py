class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def talk(self):
        print(f"{self.name}  can talk")

    def walk(self):
        print(f"{self.name}  can walk")
    def read(self):
         print(f"{self.name}  can Read")

p_obj=person("manish",30)
p_obj.talk()
p_obj.walk()
p_obj.read()


