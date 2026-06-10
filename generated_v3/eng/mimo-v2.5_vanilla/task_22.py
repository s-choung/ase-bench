from ase.build import fcc111, molecule, add_adsorbate

# Create Al(111) slab with 3 layers, 3x3 unit cells, and 10 Å vacuum
slab = fcc111('Al', size=(3, 3), layers=3, vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Adsorb N2 on bridge site at 2.0 Å height above the surface
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print number of atoms and atom types
print("Number of atoms:", len(slab))
print("Atom types:", slab.get_chemical_symbols())
