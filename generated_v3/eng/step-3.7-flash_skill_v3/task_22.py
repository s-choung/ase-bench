from ase.build import fcc111, molecule, add_adsorbate

# Build 3-layer Al(111) slab with 10 Å vacuum (10 Å per side)
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Load N2 molecule from G2 database
n2 = molecule('N2')

# Adsorb N2 on bridge site at 2.0 Å height (measured from slab surface to adsorbate center)
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print required information
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {sorted(set(slab.get_chemical_symbols()))}")
