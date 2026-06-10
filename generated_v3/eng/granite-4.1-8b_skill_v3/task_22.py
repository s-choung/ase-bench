from ase import Atoms
from ase.build import fcc111, add_adsorbate, add_vacuum
from ase.atom import Atom
from ase.molecule import molecule

# Create Al(111) 3-layer slab with vacuum
slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)

# Obtain N2 molecule
n2 = molecule('N2')

# Place N2 at bridge site with specified height
add_adsorbate(slab, n2, height=2.0, position='bridge')
# Add vacuum if not automatically done (usually handled by add_adsorbate, but ensure)
add_vacuum(slab, 10.0)

# Print the number of atoms and the types of atoms in the final structure
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {[a.symbol for a in slab]}")
