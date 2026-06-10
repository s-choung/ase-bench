from ase.build import fcc111, add_adsorbate, molecule

# Create 3-layer Al(111) slab with 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
# Load N2 molecule
n2 = molecule('N2')
# Adsorb N2 on bridge site at 2.0 Å height
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Output required structure properties
total_atoms = len(slab)
atom_types = sorted(set(slab.get_chemical_symbols()))
print(f"Total number of atoms: {total_atoms}")
print(f"Atom types present: {', '.join(atom_types)}")
