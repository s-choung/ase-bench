from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase import Atoms

# Create Pt(111) slab of 3 layers
slab = fcc111('Pt', size=(1, 1, 3), periodic=True)

# Add CO adsorbate
add_adsorbate(slab, 'CO', 1.2, 'ontop')

# Convert the slab-adsorbate system to an Atoms object (redundant here but for clarity)
system = slab

# Fix the bottom Pt layer
bottom_layer_mask = [atom.index for atom in system if atom.position[2] < system.cell[2, 2] * 2 / 3]  # Approximate bottom layer
constraint_bottom = FixAtoms(indices=bottom_layer_mask)
system.set_constraint([constraint_bottom, FixBondLength(0, 1)])  # 0 and 1 assume C is first added, then O - adjust indices to match: C index=-2, O index=-1 generally*

# For clarity: better explicit indices
# Find the indices of C and O
c_index = None
o_index = None
for atom in system:
    if atom.symbol == 'C':
        c_index = atom.index
    elif atom.symbol == 'O':
        o_index = atom.index

if c_index is None or o_index is None:
    raise RuntimeError("Failed to determine C and O indices.")

# Set fixed constraints including both FixAtoms and FixBondLength using identified indices
system.set_constraint([
    constraint_bottom,  # Already defined
    FixBondLength(c_index, o_index)
])

# Set calculator
system.set_calculator(EMT())

# Optimize with BFGS
opt = BFGS(system, trajectory='CO_Pt111.traj')
opt.run(fmax=0.05)

# Output final energy and bond length
print(f"Final energy: {system.get_potential_energy():.3f} eV")
print(f"Final C-O distance: {system.get_distance(c_index, o_index):.3f} Å")
