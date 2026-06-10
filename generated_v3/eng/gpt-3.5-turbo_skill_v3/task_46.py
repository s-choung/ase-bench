from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create Pt(111) slab with 3 layers
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Adsorb CO molecule on top of the Pt slab
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Apply constraints to fix bottom layer and C-O bond length
slab.set_constraint([FixAtoms(mask=[atom.index < len(slab)/3 for atom in slab])])
slab.set_constraint(FixBondLength(0, 1))

# Set EMT calculator
slab.calc = EMT()

# Optimize the system with both constraints
opt = BFGS(slab, trajectory='opt_CO_Pt.traj')
opt.run(fmax=0.05)

# Print the final energy and C-O distance
final_energy = slab.get_potential_energy()
co_distance = slab.get_distance(0, 1)
print(f"Final Energy: {final_energy:.2f} eV")
print(f"C-O Distance: {co_distance:.2f} Å")
