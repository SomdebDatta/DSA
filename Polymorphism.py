class USA:
    def salary(self):
        print("In USA, We give atleast 100k dollars per year to devs")

    def population(self):
        print("In USA, we have around 500M population.")

    def language(self):
        print("In USA, English is the most widely used language.")


class INDIA:
    def salary(self):
        print("In INDIA, We give 30k dollars per year to devs")

    def population(self):
        print("In INDIA, we have around 1.3B population.")

    def language(self):
        print("In INDIA, Hindi is the most widely used language.")


def implement(obj):
    obj.salary()
    obj.population()
    obj.language()


implement(USA())
implement(INDIA())
