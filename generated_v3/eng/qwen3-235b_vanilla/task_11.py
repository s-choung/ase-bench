from ase.lattice.cubic import BodyCenteredCubic

structure = BodyCenteredCubic(symbol='Al', latticeconstant=3.3, cubic=True)
print(structure.get_cell())
print(structure.get_chemical_formula())
