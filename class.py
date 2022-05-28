class Student:
    def __init__(self,name,tracks,age,score):
        self.name=str(name)
        self.age=age
        self.tracks=tracks
        self.score=float(score)

    def change_name(self,change_name,):
        self.change_name=change_name
        print("Student new name:",change_name)

    def change_age(self,change_age):
        self.change_age = change_age
        print ("student new age:",change_age)

    def add_tracks(self,add_tracks):
        self.add_tracks=add_tracks
        print("added tracks:",add_tracks)

    def get_score(self,):
        self.get_score=self.score
        print("new score get is:",self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print('name:',Bob.name)
print('age:',Bob.age)
print('score:',Bob.score)
print('tracks:',Bob.tracks)

 
 
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score()

