from ase.build import fcc
from ase.calculators import mt2
from ase.io import write
from ase.math import get_distances

atoms = fcc('Cu', size=(2, 2, 2))
write('Cu_fcc_2x2x2.vasp', atoms)

calc = mt2.EMT()
atoms.calc = calc
atoms.get_potential_energy()

distances = get_distances(atoms, 0, mic=True)

print(f"Minimum distance: {min(distances)}")
print(f"Maximum distance: {max(distances)}")
