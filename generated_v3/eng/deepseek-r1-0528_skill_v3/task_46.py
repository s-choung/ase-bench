from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Build 3-layer Pt(111) slab (1x1 surface)
slab = fcc111('Pt', size=(1, 1, 3), vacuum=10.0)

# Add CO adsorbate at fixed height
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Set tags: bottom layer=0, middle=1, top=2, adsorbate=3
tags = slab.get_tags()
tags.tolist()
tags[3:] = [3, 3]  # Assign new tags to adsorbate atoms
slab.set_tags(tags)

# Set constraints
bottom_constraint = FixAtoms(mask=(slab.get_tags() == 0))
bond_constraint = FixBondLength(-2, -1)  # Last two atoms are C and O
slab.set_constraint([bottom_constraint, bond_constraint])

# Run optimization
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output results
print(f"Final energy: {slab.get_potential_energy():.3f} eV")
print(f"C-O distance: {slab.get_distance(-2, -1):.3f} Å")
