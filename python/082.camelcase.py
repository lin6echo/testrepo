import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

e = camelcase.CamelCase()
txt = "import camelcase"
print(e.hump(txt))