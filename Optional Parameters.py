# def deltabravo(back, add=3, dump=2):
# print(back * (dump + add))
# call = deltabravo("Howdy \n", 2, 4)

class car(object):
    def __init__(self, make, model, year, condition="New", miles=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.miles = miles

        def display(self, showAll):
            if showAll:
                print("This car is a %s %s from %s, it is %s and has %s miles." %(self.make,self.model,self.year,self.condition,self.miles))
            else:
                print("This car is a %s %s from %s." %exit())


whip = car("Ford", "F-150", 2021)
whip.display(True)
