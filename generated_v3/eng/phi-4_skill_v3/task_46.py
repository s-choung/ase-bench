from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS, FIRE
from ase.thermo import atomistics.optimize.bfgs
import numpy as np

# Create a Pt(111) three-layer slab with a vacuum of 10 Angstroms
slab = fcc111('Pt', layers=3, size=(2, 2, 4), vacuum=10.0)

# Create CO molecule and adsorb it onto the slab
co = molecule('CO')

# Adsorb CO on the top layer
co_layer = slab.copy()
co_layer.surface(3) = co_layer  # Copies CO molecule to the top layer
co_layer.ase.periodic.cartesian(3, -10.5)  # Position CO in top layer center

# Ensure the PT slab's bottom layer is fixed and constrain the C-O bond length
co_layer.set_constraint(FixAtoms(mask=[a.layer == slab.layer for a in slab]))
co_layer.set_constraint([FixBondLength(co_layer.cart_of_atoms[:], co_layer.cart_of_atoms[1:]), 
                        mask=[True, True, True])

# Assign EMT calculator to the slab
slab.constraints.calc = EMT()

# Execute BFGS optimization with fmax of 0.05
BFGS_slab = BFGS(co_layer, fmax=0.05)
BFGS_slab.run()

# Final CO -O distance and energy
final_energy = EMT_bfgs.get_potential_energy(slab=co_layer).energy
final_dist = co_layer.get_distance(co_layer.get_atomic_numbers()[:1], co_layer.get_atomic_number()[1])

# Print results
print(f"Final CO position energy: {final_energy}")
print(f"Final CO-O bond length: {final_dist}")
