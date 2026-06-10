import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Build Pt(111) slab with 3 layers
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Add CO molecule at atop site
add_adsorbate(slab, 'CO', height=1.8, position='top')

# Fix bottom layer (z < 4.0 Å)
z_positions = slab.get_positions()[:, 2]
fix_bottom = FixAtoms(indices=[i for i, z in enumerate(z_positions) if z < 4.0])

# Find C and O atoms to fix bond length
symbols = slab.get_chemical_symbols()
c_idx = symbols.index('C')
o_idx = symbols.index('O')
fix_CO = FixBondLength((c_idx, o_idx))

# Apply both constraints
slab.set_constraint([fix_bottom, fix_CO])

# Calculate with EMT
slab.calc = EMT()

# Optimize structure
dyn = BFGS(slab, logfile=None)
dyn.run(fmax=0.05)

# Print results
energy = slab.get_energy()
co_distance = slab.get_distance(c_idx, o_idx)
print(f'Final energy: {energy:.3f} eV')
print(f'C-O distance: {co_distance:.3f} Å')
