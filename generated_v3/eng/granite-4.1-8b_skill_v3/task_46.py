from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.build import fcc111, add_adsorbate

# Create the Pt(111) slab with 3 layers and add vacuum
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Add CO molecule on top of the slab
co = Atoms('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Fix the bottom layer (all atoms with tag >= 3)
fixed_bottom = FixAtoms(mask=[atom.tag >= 3 for atom in slab])

# Fix the C-O bond: indices of C and O atoms
co_index = next(i for i, a in enumerate(slab) if a.symbol == 'C')
o_index = next(i for i, a in enumerate(slab) if a.symbol == 'O')
fix_c_o = FixBondLength(co_index, o_index)

# Apply both constraints to the system
slab.set_constraint([fixed_bottom, fix_c_o])

# Set calculator
slab.calc = EMT()

# Optimize
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# Print final energy and C-O distance
final_energy = slab.get_potential_energy()
co_distance = slab.get_distance(co_index, o_index)
print(f"Final energy: {final_energy:.3f} eV")
print(f"C-O distance: {co_distance:.3f} Å")
