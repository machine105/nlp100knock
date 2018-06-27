str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

one_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
atoms = dict()

str = str.replace(".", " ")
splited = str.split()

atoms = {s[0] if (i + 1) in one_list else s[0:2] : i + 1 for (i, s) in enumerate(splited)}
print(atoms)
        
        

