from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength

# Create Pt(111) slab with 3 layers and vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Add CO molecule on top site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Set calculator
slab.calc = EMT()

# Define constraints: fix bottom Pt layer (indices 0-3) and fix C-O bond
constraints = [
    FixAtoms(indices=[i for i, atom in enumerate(slab) if i < 4]),  # bottom layer
    FixBondLength(4, 5)  # C-O bond between atoms at index 4 (C) and 5 (O)
]
slab.set_constraint(constraints)

# Optimize geometry
opt = BFGS(slab, trajectory='co_adsorption.traj')
opt.run(fmax=0.05)

# Print final energy and C-O distance
energy = slab.get_potential_energy()
co_distance = slab.get_distance(4, 5)
print(f"Final energy: {energy:.3f} eV")
print(f"C-O distance: {co_distance:.3f} Å")
