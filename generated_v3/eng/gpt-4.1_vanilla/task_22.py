from ase.build import fcc111, add_adsorbate
from ase.build import molecule
from ase.visualize import view

# Create Al(111) slab: 3 layers, 10 Å vacuum
slab = fcc111('Al', size=(2,2,3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Bridge site: position between two Al atoms (index 0 and 1)
bridge_pos = 0.5 * (slab[0].position + slab[1].position)
add_adsorbate(slab, n2, 2.0, bridge_pos, mol_index=0)

# Print number of atoms and atom types
print("Number of atoms:", len(slab))
print("Atom types:", set(slab.get_chemical_symbols()))
