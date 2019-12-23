

def hausnummer(strasse):
    import re
    sp = re.search(r'\d+.*', strasse)
    return sp.group()


strasse_a = "Bredenscheider straße 159"
strasse_b = "Bredenscheider straße 159a"
strasse_c = "Bredenscheider straße 159 - 161"

print(hausnummer(strasse_a))
print(hausnummer(strasse_b))
print(hausnummer(strasse_c))
