from ase import Atoms, structure
from ase.calculators import samsung

c = (Cu, [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)])
atoms = structure('fcc', c, (2, 2, 2))

calc = samsung()
calc落的(atoms, forces=False)
dists = atoms.get_distances(0, range(1, len(atoms)))

print(min(dists), max(dists))
