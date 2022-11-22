calls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

staff = ["anna", "ben", "cherry"]
staff_count = len(staff)
early_staff = 2
early_calls = calls[:5]

# This code snippet selects every second early call
# and applies it to the early staff and stores in a dictionary.
early_allocation = {}
for employee in staff[:early_staff]:
    position = staff.index(employee)
    early_allocation[employee] = early_calls[position::early_staff]

print(early_allocation)

# This code snippet selects every second late call
# and applies it to the late staff and stores in a dictionary.
late_calls = calls[5:]
late_staff = staff[::-1]
late_allocation = {}

for employee in late_staff:
    position = late_staff.index(employee)
    late_allocation[employee] = late_calls[position::staff_count]

print(late_allocation)
