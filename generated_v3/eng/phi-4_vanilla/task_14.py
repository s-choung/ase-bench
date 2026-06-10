from ase.build import bulk
from ase.spacegroup import crystal
import ase

# Define lattice constant and space group
lattice_constant = 5.64
spacegroup = 225  # Fm-3m
species = ['Na', 'Cl']
positions = [(0, 0, 0), (0.5, 0.5, 0.5)]

# Create NaCl crystal structure
nacl_crystal = crystal(symbols=species, cell=lattice_constant * [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 
                       a=lattice_constant, spacegroup=spacegroup, 
                       positions=positions)

# Output the number of atoms and chemical symbols
num_atoms = nacl_crystal.get_global_number_of_atoms()
chemical_symbols = nacl_crystal.get_chemical_symbols()

print(f"Number of atoms: {num_atoms}")
print(f"Chemical symbols: {chemical_symbols}")
