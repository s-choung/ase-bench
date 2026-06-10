from ase.build import fcc111, add_adsorbate, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build 3-layer Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Add CO adsorbate
co = molecule('CO')
add_adsorbate(slab, co, height=2.0, position='ontop')

# Get indices for constraints
# Bottom layer: tag == 0 (layers tagged from bottom: 0,1,2 for 3 layers)
bottom_indices = [atom.index for atom in slab if atom.tag == 0]

# Find C and O indices (last two atoms after adding adsorbate)
c_idx = len(slab) - 2  # C atom
o_idx = len(slab) - 1  # O atom

# Apply constraints
constraints = [
    FixAtoms(indices=bottom_indices),
    FixBondLength(c_idx, o_idx)
]
slab.set_constraint(constraints)

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

# Get results
energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)

print(f"Final energy: {energy:.4f} eV")
print(f"C-O distance: {co_dist:.4f} Å")
