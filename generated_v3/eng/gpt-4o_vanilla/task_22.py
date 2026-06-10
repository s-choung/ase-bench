from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

# Create an Al(111) surface
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Create an N2 molecule
n2 = molecule('N2')

# Add N2 to the bridge site
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Set up and run the EMT calculator
slab.calc = EMT()
energy = slab.get_potential_energy()

# Print the number of atoms and atom types
num_atoms = len(slab)
atom_types = set(slab.get_chemical_symbols())
print(f'Number of atoms: {num_atoms}')
print(f'Atom types in the structure: {atom_types}')
