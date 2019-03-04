class Paperboy:
    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__(self):
        return "{} delivered {} papers and made ${}.".format(
            self.name, self.experience, self.earnings
        )

    def quota(self):
        return 50 + (self.experience / 2)

    def deliver(self, start_address, end_address):
        current_quota = self.quota()
        number of_houses = abs(end_address - start_address) + 1
        if number_of_houses >= current_quota:
            self.earnings += 0.25 * (
                current_quota + 2 * (number_0f_houses - current_quota)
            )
        else:
            self.earnings += 0.25 * number_0f_houses - 2
        self.experience += number_0f_houses

    def report(self):
        return "I'm {},delivered {} papers and earned ${:.2f}".format(
            self.name, self.experience, self.earnings
        )


tommy = Paperboy("Tommy")
print(tommy)

print(tommy.quota())
print(tommy.deliver(101, 160))
print(tommy.earnings)
print(tommy.report())

print(tommy.quota())
print(tommy.deliver(1, 75))
print(tommy.earnings)
print(tommy.report())
