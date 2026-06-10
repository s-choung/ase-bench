from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Add CO molecule
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Apply constraints
constraints = [
    FixAtoms(mask=[atom.tag < 3 for atom in slab]),  # Fix bottom layer
    FixBondLength(slab.indices[-2], slab.indices[-1])  # Fix C-O bond
]
slab.set_constraint(constraints)

# Set calculator and optimize
slab.calc = EMT()
dyn = BFGS(slab)
dyn.run(fmax=0.05)

# Print final energy and C-O distance
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
co_distance = slab.get_distance(slab.indices[-2], slab.indices[-1])
print(f"C-O distance: {co_distance:.4f} Å")
