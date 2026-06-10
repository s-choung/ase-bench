from ase.lattice.cubic import BodyCenteredCubic
al = BodyCenteredCubic('Al', latticeconstant=3.3, cubic=True)
print(al.cell)
print(al.get_chemical_formula())
