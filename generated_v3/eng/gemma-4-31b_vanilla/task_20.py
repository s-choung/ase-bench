from ase.build import nanotube
from ase.calculators.emt import EMT

# Create (6,6) carbon nanotube with length 4 Angstroms
atoms = nanotube(6, 6, length=4.0)
atoms.calc = EMT()

print(f"Number of atoms: {len(atoms)}")
print(f"Cell info:\n{atoms.get_cell()}")
