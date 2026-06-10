from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms, FixBondLengths
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Pt(111) 3-layer slab with 4x4 surface and vacuum
slab = fcc111('Pt', size=(4, 4, 3), vacuum=10.0)

# Add CO adsorbate: C on top site, O 1.1 Å above C along surface normal
# Find top site position (center of 4-fold hollow)
surface = slab[:16]  # Top layer atoms
pos_surface = surface.get_positions()
center = pos_surface.mean(axis=0)
top_site = center + [0, 0, 2.0]  # 2 Å above surface

# Add C and O atoms: C at top_site, O along +z direction
co_atoms = Atoms('CO', positions=[top_site, top_site + [0, 0, 1.1]])
slab.extend(co_atoms)

# Fix bottom layer (last 16 atoms)
fix_bottom = FixAtoms(indices=[atom.index for atom in slab[-16:]])

# Fix C-O bond length (indices of C and O: last two atoms)
fix_bond = FixBondLengths([[slab.get_global_index(-2), slab.get_global_index(-1)]])

# Set calculator and apply constraints
slab.set_calculator(EMT())
slab.set_constraint([fix_bottom, fix_bond])

# Optimize
opt = BFGS(slab)
opt.run(fmax=0.05)

# Print results
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(-2, -1):.4f} Å")
