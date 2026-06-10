from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength

# Build Pt(111) slab and CO molecule
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')

# Add CO to the slab
add_adsorbate(slab, co, height=1.8, position='ontop')

# Define constraints
n_pt_atoms = len(slab) - len(co)
c_index = n_pt_atoms
o_index = n_pt_atoms + 1

fix_bottom = FixAtoms(mask=[a.tag < 3 for a in slab])
fix_bond = FixBondLength(c_index, o_index)

# Apply both constraints
slab.set_constraint([fix_bottom, fix_bond])

# Set calculator and optimize
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

# Print results
final_energy = slab.get_potential_energy()
co_distance = slab.get_distance(c_index, o_index)

print(f'Final energy: {final_energy:.3f} eV')
print(f'Final C-O distance: {co_distance:.3f} Å')
