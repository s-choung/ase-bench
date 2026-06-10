from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import write, read

# Create a copper (Cu) FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)  # 3.6 Å is a reasonable lattice parameter for Cu
atoms.calc = EMT()

# Save the structure in VASP POSCAR format
write('Cu_fcc.poscar', atoms, format='vasp')

# Read the structure back
atoms_read = read('Cu_fcc.poscar', format='vasp')

# Print the number of atoms
print("Number of atoms:", len(atoms_read))

# Get and print cell parameters (a, b, c, α, β, γ)
cell = atoms_read.get_cell()
cell_lengths = cell.lengths()
cell_angles = cell.angles()

print("Cell parameters:")
print("a = {:.3f} Å, b = {:.3f} Å, c = {:.3f} Å".format(*cell_lengths))
print("α = {:.2f}°, β = {:.2f}°, γ = {:.2f}°".format(*cell_angles))
