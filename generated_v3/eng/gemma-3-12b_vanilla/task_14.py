from ase.build import fcc
from ase.calculators.emt import EMT
from ase.io import write

atoms = fcc('NaCl', size=2, symbol='Na', latticeconstant=5.64)
atoms.set_positions('frac')
cl_pos = [(0.5, 0.5, 0.5)]
atoms.replace(atoms.specie[0], atoms.specie[1], cl_pos)
calc = EMT()
atoms.calc = calc

print(len(atoms))
for atom in atoms:
    print(atom.symbol)

write('NaCl.xyz', atoms)
