from ase.io import write, read
from ase.build import bulk

# Build Cu FCC structure
atoms = bulk('Cu', 'fcc', a=3.6)

# Write VASP POSCAR
write('POSCAR', atoms, format='vasp')

# Read structure back from POSCAR
read_atoms = read('POSCAR', format='vasp')

# Print analysis
print("Number of atoms:", len(read_atoms))
print("Cell parameters:")
for i, vec in enumerate(read_atoms.cell, start=1):
    print(f"Vector {i}:", vec)
lengths_angles = read_atoms.get_cell_lengths_and_angles()
print(f"Lattice: a={lengths_angles[0]:.4f} Å, b={lengths_angles[1]:.4f} Å, "
      f"c={lengths_angles[2]:.4f} Å, α={lengths_angles[3]:.2f}°, "
      f"β={lengths_angles[4]:.2f}°, γ={lengths_angles[5]:.2f}°")
