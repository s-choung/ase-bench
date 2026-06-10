from ase.build import fcc100
from ase.calculators.emt import EMT

atoms = fcc100('Cu', size=(3,3,3), vacuum=12.0)
calc = EMT()
atoms.calc = calc

print(f"Number of atoms: {len(atoms)}")
print("Cell info:")
print(atoms.get_cell())
