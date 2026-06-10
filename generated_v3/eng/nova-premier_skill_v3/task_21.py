from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

# Au icosahedron
atoms = Icosahedron('Au', noshells=3, latticeconstant=4.08)
atoms.calc = EMT()

# Compute COM
pos = atoms.get_positions()
com = pos.mean(axis=0)

print(f"Atoms: {len(atoms)}")
print(f"Center: [{com[0]:.4f}, {com[1]:.4f}, {com[2]:.4f}] Å")
