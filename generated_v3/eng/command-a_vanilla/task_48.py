from ase.lattice.cubic import FaceCenteredCubic
from ase.geometry import get_distances

atoms = FaceCenteredCubic(directions=[[1,0,0], [0,1,0], [0,0,1]],
                          size=(2,2,2), symbol='Cu', pbc=True)

distances = get_distances(atoms, 0, atoms.indices, mic=True)[0]

print(f"Minimum distance: {min(distances):.4f} Å")
print(f"Maximum distance: {max(distances):.4f} Å")
