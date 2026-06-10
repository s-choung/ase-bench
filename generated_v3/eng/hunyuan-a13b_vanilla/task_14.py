from ase import *
from ase.lattice import cubic

# Create NaCl structure
lattice_constant = 5.64  # in angstroms
a = cubic(lattice_constant)
nacl = a.get_atom_positions()

# Atoms at (0,0,0) (Na) and (0.5,0.5,0.5) (Cl)
positions = [[0.0, 0.0, 0.0, 'Na'],
            [0.5, 0.5, 0.5, 'Cl']]
mol = Atoms(positions,reject_duplicates=True)
mol.cell = a.cell
mol.pbc = True

# Print info
print(mol.natoms)
print(' '.join([symbol for symbol in mol.symbols]))
