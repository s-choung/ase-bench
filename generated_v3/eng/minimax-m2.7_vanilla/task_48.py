from ase.build import bulk
from ase.geometry import get_distances

# Create a Cu FCC bulk 2x2x2 supercell
Cu = bulk('Cu', 'fcc', a=3.615)   # typical Cu lattice constant (Å)
Cu = Cu * (2, 2, 2)

# Position of atom 0 and all other atoms
pos0 = Cu[0].position
other_pos = Cu[1:].positions

# Compute distances with minimum-image convention (mic=True)
distances = get_distances(pos0, other_pos, cell=Cu.cell, pbc=Cu.pbc, mic=True)

print('Minimum distance:', distances.min())
print('Maximum distance:', distances.max())
