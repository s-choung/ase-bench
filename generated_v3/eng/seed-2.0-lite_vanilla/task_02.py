from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

# Create 4-layer Pt(111) slab with 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), a=3.98, vacuum=10.0)

# Build CO molecule (C-O bond length 1.14 Å)
co_mol = Atoms('CO', positions=[[0, 0, 0], [0, 0, 1.14]])

# Add CO ontop site, C placed 1.9 Å above surface Pt atom
add_adsorbate(slab, co_mol, height=1.9, position=(0, 0))

# Assign built-in EMT calculator
slab.set_calculator(EMT())

# Print total number of atoms in final structure
print(len(slab))
