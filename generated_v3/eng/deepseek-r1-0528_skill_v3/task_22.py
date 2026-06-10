from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Al', size=(1,1,3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

num_atoms = len(slab)
atom_types = set(slab.get_chemical_symbols())

print("Number of atoms:", num_atoms)
print("Atom types:", ', '.join(sorted(atom_types)))
