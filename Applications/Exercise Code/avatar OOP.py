# THE AVATAR CLASS - by Moria Merriweather
# This is similar to quiz 6a problem 7 and problem 8, about BankAccount


class Avatar:
    def __init__(self, name, hair, initial_gold):
        self.name = name
        self.hair = hair
        self.initial_gold = initial_gold
        self.bag = self.initial_gold
        self.buried = 0.0

    def find_gold(self, amount):
        self.bag += amount

    def bury_gold(self, amount):
        self.buried += amount
        self.bag -= amount

    # SPRINKLED_WITH_FAIRY_DUST METHOD:
    def sprinkled_with_fairy_dust(self):
        self.bag += self.bag * 0.1

    def __str__(self):
        return 'Name: ' + self.name + '\nBag: ' + str(self.bag) + '\nBuried: ' + str(self.buried)

# ==>  Wild Girl should have 5.75 gold in bag, and 2.5 gold buried.
# ==>  Mad Max should have 28.3195 gold in bag, and 21.5 gold buried.


wildgirl = Avatar("Wild Girl", "purple", 5.5)
wildgirl.find_gold(2.0)
wildgirl.sprinkled_with_fairy_dust()
wildgirl.bury_gold(2.5)
print(wildgirl)
madmax = Avatar("Mad Max", "black", 6.5)
madmax.find_gold(25.0)
madmax.bury_gold(2.0)
madmax.sprinkled_with_fairy_dust()
madmax.bury_gold(4.5)
madmax.sprinkled_with_fairy_dust()
madmax.find_gold(10.0)
madmax.bury_gold(15.0)
madmax.sprinkled_with_fairy_dust()
print("==============================")
print(madmax)
