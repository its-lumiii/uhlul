class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            print("Salary cannot be negative.")
        else:
            self._salary = amount
            print("Salary is not negative.")

e = Employee("Sam", 50000)
e.salary = 55000
e.salary = -1000
