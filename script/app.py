from balaboba import Balaboba

bb = Balaboba()
# Get text types
intros = bb.intros(language="ru")
# Get the first text type
intro = next(intros)
# 11 народные мудрости
# 13 ?
# 14 ?
# 15 ?
# Print Balaboba's response to the "Hello" query
response = bb.balaboba("Деньги", intro=11)
print(response)