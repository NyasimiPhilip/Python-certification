class Category:
  def __init__(self, name):
    self.name = name
    self.total = 0.0
    self.ledger = []

  def __repr__(self):
    s = f"{self.name:*^30}\n"
    acc = 0

    for item in self.ledger:
      s += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
      acc += item["amount"]

    s += f"Total: {self.total:.2f}"
    return s

  def deposit(self, amount, description=""):
    self.total += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    can_withdraw = self.check_funds(amount)

    if can_withdraw:
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})

    return can_withdraw

  def get_balance(self):
    return self.total

  def transfer(self, amount, to_category):
    can_transfer = self.check_funds(amount)

    if can_transfer:
      self.withdraw(
        amount,
        f"Transfer to {to_category.name}")
      to_category.deposit(
        amount,
        f"Transfer from {self.name}")

    return can_transfer

  def check_funds(self, amount):
    return amount <= self.total


def create_spend_chart(categories):
  s = "Percentage spent by category\n"

  total = 0
  cats = {}
  for cat in categories:
    cat_total = 0
    for item in cat.ledger:
      amount = item["amount"]
      if amount < 0:
        total += abs(amount)
        cat_total += abs(amount)

    cats[cat.name] = cat_total

  cats = {
    k: (v / total) * 100
    for k, v in cats.items()
  }

  dash_width = len(cats) * 3 + 1
  spaces = dash_width - 1
  for n in range(100, -1, -10):
    s += f"{n:>3}| "
    bar_row = []
    for val in cats.values():
      row_val = [' '] * 3
      if val >= n:
        row_val[0] = "o"
      bar_row += row_val
    s += f"{''.join(bar_row)}{' ' * (spaces - len(bar_row))}\n"
    
  s += f"{' ' * 4}{'-' * dash_width}\n"

  cat_names = [list(name) for name in cats]
  while any(cat_names):
    s += f"{' ' * 4}"
    for name in cat_names:
      s += f" {' ' if not name else name.pop(0)} "
    s += " \n"
  # Need to add strip to remove the newline character for last line and then add back the spaces. If anyone has a better solution, let me know :)
  s = s.strip() + '  '

  # print(s)
  return s


food = Category("food")
entertainment = Category("entertainment")
business = Category("business")
# food.deposit(100, "something")
# food.withdraw(20, "beans")
# food.transfer(25.5, entertainment)
# entertainment.deposit(500, "movies")
# entertainment.withdraw(125, "black widow")
# entertainment.withdraw(50, "nobody")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
print(actual)
# create_spend_chart([food, entertainment])
