from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Get indices for constraints
bottom_layer_indices = [a.index for a in slab if a.tag == 0]
co_indices = [a.index for a in slab if a.symbol in ['C', 'O']]
c_index, o_index = co_indices

# Apply constraints
constraint1 = FixAtoms(indices=bottom_layer_indices)
constraint2 = FixBondLength(c_index, o_index)
slab.set_constraint([constraint1, constraint2])

# Optimization
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Print final energy and C-O distance
final_energy = slab.get_potential_energy()
co_distance = slab.get_distance(c_index, o_index)
print(f"Final energy: {final_energy} eV")
print(f"C-O distance: {co_distance} Å")
