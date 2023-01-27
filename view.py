
def New_employee():
    a = str((input("Input name: "))+';')
    b = str(input("Input surname: ")+';')
    c = str(input("Input status: ")+';')
    d = str(input("Input tel/number: "))
    lst= a+b+c+d
    element = list(lst.split(';'))
    return element
