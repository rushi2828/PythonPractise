num = 20
num1 = 12


class SampleConstructor:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("ID:%d\nName:%s" % (self.id, self.name))

    def add(self, num, num1):
        num2 = num + num1
        return num2

    def newFun(self):
        a = num - num1
        return a


sc = SampleConstructor(2, "Test")
sc1 = SampleConstructor(3, "Test1")

# print(sc.num)
sc.display()
sc1.display()

print(sc.add(12, 89))

print(sc.newFun())
print(sc1.newFun())
