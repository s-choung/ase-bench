from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))

distances = get_distances(atoms[0], atoms, cell=atoms.cell, pbc=True, mic=True)[0]

print(f"Minimum distance: {distances[1:].min():.6f} Å")
print(f"Maximum distance: {distances[1:].max():.6f} Å")
