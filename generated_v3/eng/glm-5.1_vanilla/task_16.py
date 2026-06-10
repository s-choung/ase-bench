from ase.lattice.surface import bcc110
from ase.calculators.emt import EMT

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10)
atoms.calc = EMT()

print(f"Number of atoms: {len(atoms)}")
print(f"Cell size:\n{atoms.cell}")
