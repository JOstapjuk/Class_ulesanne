
class Student:
    """ Student class """

    def hello(self):
        print("Hello! ",self.title,self.name)

    def greet_friend(self,friend_name):
        print("Hello, " +friend_name)

    def __init__(self,name,title,age):
        self.name = name
        self.title = title
        self.age = age

    def greet_Leela (self):
        if self.name == "Leela":
            print("Greetings Leela, long time no see")
        else:
            print("Hello stranger")

    def upgrade(self):
        self.age += 1



s = Student("Ago","Teacher",30)
print(type(s))
print(id(s))
s.hello()
s.greet_friend("Ago")
print(s.name,s.title)
s.upgrade
print(s.age)

t = Student("Leela","Captain",55)
print(type(t))
print(id(t))
print(t.name,t.title)
for i in range(4):
    t.upgrade()
print(t.age)

s3 = s
print(type(s3))
print(id(s3))

if s == s3:
    print("true")
else:
    print("false")

t.greet_Leela()