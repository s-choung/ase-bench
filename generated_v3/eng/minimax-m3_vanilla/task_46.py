from ase.build import fcc111
from ase import Atoms
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create Pt(111) slab with 3 layers
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, a=3.92)

# Get atop site coordinates (top layer Pt atom)
z_top = max(a.position[2] for a in slab if a.symbol == 'Pt')
top_pt = next(a for a in slab if a.symbol == 'Pt' and abs(a.position[2] - z_top) < 0.1)
x, y = top_pt.position[0], top_pt.position[1]

# Add CO at atop site (C down)
c_pos = [x, y, z_top + 1.85]
o_pos = [x, y, z_top + 1.85 + 1.14]
slab += Atoms('CO', positions=[c_pos, o_pos])

# Identify bottom layer Pt atoms
pt_atoms = [a for a in slab if a.symbol == 'Pt']
z_bottom = min(a.position[2] for a in pt_atoms)
bottom_idx = [a.index for a in pt_atoms if abs(a.position[2] - z_bottom) < 0.1]

# Apply both constraints simultaneously
slab.set_constraint([FixAtoms(indices=bottom_idx),
                     FixBondLength(-2, -1)])  # C-O bond

# Optimize with EMT and BFGS
slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.05)

# Print final results
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(-2, -1):.4f} Angstrom")
