from ase.lattice.surface import fcc100
from ase.build import add_vacuum

atoms = fcc100('Cu', size=(3, 3, 3))
add_vacuum(atoms, 12.0)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell info: {atoms.cell}")
