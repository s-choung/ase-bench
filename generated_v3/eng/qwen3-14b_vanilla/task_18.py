from ase import Atoms
from ase.molecules import methane

atoms = methane()
print("Atomic coordinates:")
print(atoms.get_positions())
print("Bond lengths:")
c = atoms[0]
for h in atoms[1:]:
    print(c.get_distance(h))
print("Chemical formula:", atoms.get_chemical_formula())
