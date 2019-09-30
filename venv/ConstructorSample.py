class SampleConstructor:
    num = 10

    def __init__(self, id, name):
        self.id = id;
        self.name = name;

    def display(self):
        print("ID:%d\nName:%s" % (self.id, self.name))


sc = SampleConstructor(2, "Test")
sc1 = SampleConstructor(3, "Test1")

print(sc.num)
sc.display()
sc1.display()
