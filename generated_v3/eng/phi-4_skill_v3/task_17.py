from ase.build import surface

# Create a general (2,1,1) surface from Copper bulk with 3 layers
atoms = surface('Cu', n_layers=3, miller_index=(2, 1, 1))

# Add 10 Angstroms of vacuum in z-direction
atoms.add_constraint(FixAtoms(adsorbate=atoms.constraints, atoms=atoms, mask=[False]*3 + [True]*3))

# Output the number of atoms and cell parameters
print(f"Number of atoms: {len(atoms)}")
print(f"Original cell: {atoms.get_cell()}")
print(f"Cell lengths: {atoms.get_cell_lengths()}")
print(f"Cell angles: {atoms.get_cell_angles()}")

# Export the geometry (optional for demonstration)
from ase.io import write
write('vib', atoms)
