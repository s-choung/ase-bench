from ase import Atoms
from ase.build import fcc111, add_adsorbate, FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write
import numpy as np

# Create a Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Create a CO molecule
co = Atoms([(0, 0, 0), (1.036, 0.406, 0.390)],
            cell=np.eye(3),
            positions=np.array([[0.0, 0.0, 0.0], [1.036, 0.406, 0.390]]),
            symbols=['Pt', 'C', 'O'])

# Add the CO molecule to the slab
add_adsorbate(slab, co, height=1.8, position='ontop')

# Fix the bottom layer atoms
bottom_layer_indices = [atom.tag for atom in slab if atom.position[2] < 0.5]
slab.set_constraint(FixAtoms(indices=bottom_layer_indices))

# Fix the C-O bond length
bond_distance = np.linalg.norm(co[1] - co[2])
slab.set_constraint(FixBondLength(co[0], co[2]))

# Calculate the energy and get the C-O distance
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Print the final energy and C-O distance
print("Final Energy:", slab.get_potential_energy())
print("C-O Distance:", np.linalg.norm(co[0] - co[2]))

# Write the optimized structure to a POSCAR file
write('Pt_CO.poscar', slab, format='vasp')
