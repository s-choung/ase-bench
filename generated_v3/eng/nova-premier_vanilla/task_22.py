from ase import Atoms
from ase.lattice.surface import surface
from ase.build import molecule, add_adsorbate

# Create Al(111) slab with 3 layers
slab = surface('Al', (1, 1, 1), 3, vacuum=10)

# Create and position N2 molecule above the slab
n2 = molecule('N2')
add_adsorbate(slab, n2, 2.0, 'bridge')

# Print number of atoms and types
print(len(slab), set(slab.get_chemical_symbols()))
