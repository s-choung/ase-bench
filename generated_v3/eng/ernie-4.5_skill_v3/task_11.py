from ase import Atoms
from ase.build import bulk

# Create BCC aluminum with a=3.3 Å, cubic supercell
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print cell parameters and chemical formula
print("Cell parameters (a, b, c, α, β, γ):", atoms.get_cell_lengths_and_angles())
print("Chemical formula:", atoms.get_chemical_formula())
