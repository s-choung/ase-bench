from ase import Atoms, Atom
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
add_adsorbate(slab, Atom('C', [7.0, 7.0, 15.0]), height=1.8, position=(0, 0))
add_adsorbate(slab, Atom('O', [7.0, 7.0, 15.0]), height=1.2, position=(0, 0))
co_indices = [len(slab) - 2, len(slab) - 1]
slab.set_angle(co_indices[0], co_indices[1], 180)

# Fix bottom Pt layer
mask = [atom.tag == 3 for atom in slab]
fix_bottom = FixAtoms(mask=mask)

# Fix C-O bond
fix_bond = FixBondLength(co_indices[0], co_indices[1])

# Apply constraints
slab.set_constraint([fix_bottom, fix_bond])

# Calculator
slab.calc = EMT()

# Optimize
opt = BFGS(slab, fmax=0.05)
opt.run()

# Output
print(f"Final energy: {slab.get_potential_energy():.3f} eV")
co_distance = slab.get_distance(co_indices[0], co_indices[1])
print(f"C-O distance: {co_distance:.3f} Å")
