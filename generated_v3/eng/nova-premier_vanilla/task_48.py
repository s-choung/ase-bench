from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic

cu = FaceCenteredCubic('Cu')
cu *= (2, 2, 2)
cu.set_calculator('EMT')
distances = cu.get_distances(0, cu.positions[1:], mic=True)
print(f"Min: {distances.min():.3f}, Max: {distances.max():.3f}")
