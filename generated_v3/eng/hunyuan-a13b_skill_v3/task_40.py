from ase import Atoms
from ase.io import write, read

# Create NaCl crystal structure
atoms = Atoms(
    symbols='Na Cl',
    positions=[(0, 0, 0), (0, 0, 0.5)],
    cell=[
        [0.5, 0.5, 0.5],
        [0.5, 0.5, 0],
        [0.5, 0, 0.5]
    ],
    pbc=True
)

# Save in CIF format
write('nacl.cif', atoms, format='cif')

# Read back the structure
atoms_read = read('nacl.cif', format='cif')

# Print spacegroup information
from ase.spacegroup import crystal
sg_info = crystal('NaCl', atoms_read.get_cell(), atoms_read.get_positions())
print(f"Spacegroup: {sg_info.spacegroup}")

# Print number of atoms
print(f"Number of atoms: {len(atoms_read)}")
