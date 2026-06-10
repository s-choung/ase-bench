from ase import Atoms
from ase.build import bulk, make_supercell

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc')

# Generate 2x2x2 supercell
supercell = make_supercell(atoms, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])

# Print cell information and number of atoms
print("Cell parameters (a, b, c, α, β, γ):", supercell.get_cell_lengths_and_angles())
print("Number of atoms:", len(supercell))
