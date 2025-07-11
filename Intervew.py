class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def talk(self):
        print(f"{self.name}  can talk")

p_obj=person("manish",30)
p_obj.talk()



