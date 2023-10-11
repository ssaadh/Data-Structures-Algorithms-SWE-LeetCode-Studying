class Customer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __getitem__(self):
      return 'hi'


class LunchLine:
    def __init__(self, customers: list, time_end: int) -> None:
        self.time_end = time_end
        self.line_size = len(customers)
        self.customers = customers
        
    def line_size(self) -> int:
        return self.line_size
        
    def get_customers(self) -> list:
        return self.customers

    def is_lunch_over(self) -> bool:
        current_time = 5
        if current_time > self.time_end:
            return True
        return False

lst = [Customer('sad', 5), Customer('nn', 10)]
ll = LunchLine(lst, time_end = 6)

print(ll.line_size())
print(ll.get_customers())
print(ll.is_lunch_over())
