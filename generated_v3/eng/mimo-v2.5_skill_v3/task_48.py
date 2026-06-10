from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)

d, _ = get_distances(atoms[0].position, atoms.positions, mic=True, cell=atoms.get_cell(), pbc=True)

print(f"Min distance: {d.min():.4f} Å")
print(f"Max distance: {d.max():.4f} Å")
