from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)

# Add CO adsorbate
add_adsorbate(slab, 'CO', height=1.5, position='ontop')

# Identify bottom layer atoms (fixed)
z_positions = slab.get_positions()[:,2]
bottom_indices = [i for i in range(len(slab)) if z_positions[i] < min(z_positions) + 0.5]

# Identify C and O indices (assume adsorbate atoms are last two)
c_index = len(slab) - 2
o_index = len(slab) - 1

# Set constraints
constraints = [FixAtoms(bottom_indices), FixBondLength(c_index, o_index, slab.get_distance(c_index, o_index))]
slab.set_constraint(constraints)

# Optimize
slab.calc = EMT()
dyn = BFGS(slab)
dyn.run(fmax=0.05)

# Output
energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_index, o_index)
print(f"Energy: {energy:.3f} eV")
print(f"C-O distance: {co_dist:.3f} Å")
