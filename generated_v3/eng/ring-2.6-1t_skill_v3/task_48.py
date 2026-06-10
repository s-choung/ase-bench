from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
d = get_distances(0, atoms.positions[1:], cell=atoms.cell, pbc=True, mic=True)[0]
print(f'min={d.min():.4f} Å, max={d.max():.4f} Å')
