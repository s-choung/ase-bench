from ase.build import bulk
from ase import Atoms

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)

# Generate 2x2x2 supercell
supercell = atoms.repeat((2, 2, 2))  # Alternatively: supercell = atoms * (2, 2, 2)

# Get cell information
cell_info = supercell.get_cell_lengths_and_angles()

# Print results
print(f"Number of atoms: {len(supercell)}")
print("Cell lengths and angles (a, b, c, α, β, γ):")
print(cell_info)
