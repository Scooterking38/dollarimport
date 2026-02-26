import dollarimport

dollarimport.enable()

x = 5
assert ${x} == 5
y = 10
assert ${y} + 5 == 15
def add(a,b):
    return ${a}+${b}
assert add(3,4)==7
