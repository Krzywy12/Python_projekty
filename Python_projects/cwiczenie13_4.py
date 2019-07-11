#        KOMPOZYCJA      kon "ma" jezdzca

class Horse():
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self,name):
        self.name = name

rider1 = Rider("Harry")
khan = Horse("Khan",rider1)
print(khan.rider.name)
