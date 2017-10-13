a = "У лукоморья дуб зелёный"
print(a)
a[2] = "Л"
print(a[2:11])
b = ["Арамен", "человек шашлык", "тор"]
print(b[0])
# b.append(input("добавь нового песонажа: "))
print(b)
b.insert(2, "Халк")
print(b)
del b[1]
print(b)
b.remove("Арамен")
print(b)
jl = ["Флэш", "Чудо-женщина"]
b.extend(jl)
b += jl
print(b)