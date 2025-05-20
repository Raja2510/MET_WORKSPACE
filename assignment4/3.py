employee={
    "id":101,
    "name":"michael",
    "department":"sales"
}

employee.get("salary","not disclosed")
employee.update({"salary":50000,"email":"michael@company.com"})
a=employee.popitem()
print(a)
employee_backup=employee.copy()
print("department" in employee)