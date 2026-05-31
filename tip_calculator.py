def calculate_tip(bill, tip_percent):

    tip = bill * tip_percent / 100
    total = bill + tip

    return {
        "tip": tip,
        "total": total
    }

print(calculate_tip(1000, 10))
print(calculate_tip(500, 5))
print(calculate_tip(2000, 15))