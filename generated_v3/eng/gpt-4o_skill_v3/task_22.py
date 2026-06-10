from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import write
from ase.build import molecule

# Create an Al(111) 3-layer slab with vacuum
slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)

# Create an N2 molecule
n2 = molecule('N2')

# Adsorb N2 on the bridge site
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Set the calculator
slab.calc = EMT()

# Output number of atoms and types
num_atoms = len(slab)
atom_types = slab.get_chemical_symbols()
print(f"Number of atoms: {num_atoms}")
print(f"Atom types: {set(atom_types)}")
