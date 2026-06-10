from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (2, 2, 2)
atoms.set_calculator(EMT())

print(f"Cell: {atoms.get_cell()}")
print(f"Number of atoms: {len(atoms)}")
