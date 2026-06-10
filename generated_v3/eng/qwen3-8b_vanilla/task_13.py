from ase.build import diamond
si = diamond(a=5.43, size=(3,3,3))
print(len(si))
print(si.get_volume())
