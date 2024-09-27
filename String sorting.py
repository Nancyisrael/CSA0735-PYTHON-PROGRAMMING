def sort_names(names, order):
    if order.upper() == 'A':
        return sorted(names)
    elif order.upper() == 'D':
        return sorted(names, reverse=True)
    else:
        return "Invalid order. Please enter A for Ascending or D for Descending."

names = input("Enter the names separated by space: ").split()
order = input("Order (A/D): ")

print(sort_names(names, order))
