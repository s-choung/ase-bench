from ase.build import fcc100
from ase import Atoms

slab: Atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0, orthogonal=True)
print(f"Number of atoms: {len(slab)}")
print(f"Cell info:\n{slab.cell}")
