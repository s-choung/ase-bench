from ase.build import bulk
from ase.io import read, write

# Create the NaCl bulk structure using space group Fm-3
atoms = bulk('NaCl', spacegroup=225,
             cellpar=[5.64, 5.64, 5.64, 
                      90, 90, 90], 
                      a=atoms[0], 
                      b=atoms[1], 
                      c=atoms[2])

# Check the number of atoms and chemical symbols
num_atoms = len(atoms)
chemical_symbols = sorted(set(atom.symbol for atom in atoms))

print(f"Number of atoms: {num_atoms}")
print(f"Chemical symbols: {chemical_symbols}")

# Optional: visualize or output the structure
# view(atoms)  # Uncomment to visualize the structure

# Optionally save the structure to a file (e.g., POSCAR format for VASP)
write('NaCl_fcc_poscar', atoms, format='vasp')
