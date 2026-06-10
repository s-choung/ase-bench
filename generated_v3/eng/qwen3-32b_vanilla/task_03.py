from ase import Atoms
import numpy as np

a = 3.16
u = 0.338

mo_pos = (0, 0, 0.5)
s1_pos = (0, a * np.sqrt(3)/3, 0.5 + u)
s2_pos = (a / 2, a * np.sqrt(3)/6, 0.5 - u)

atoms = Atoms(
    symbols=['Mo', 'S', 'S'],
    positions=[mo_pos, s1_pos, s2_pos],
    cell=[
        [a, 0, 0],
        [-a/2, a * np.sqrt(3)/2, 0],
        [0, 0, 1.0]
    ],
    pbc=[True, True, False]
)

z_positions = [atom.position[2] for atom in atoms]
min_z = min(z_positions)
max_z = max(z_positions)
slab_thickness = max_z - min_z

new_c = slab_thickness + 10.0
atoms.set_cell([atoms.cell[0], atoms.cell[1], [0, 0, new_c]], scale_atoms=False)

print("Final cell size (Å):")
print(atoms.get_cell())
