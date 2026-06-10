from ase import Atoms
from ase.build import bulk

# Build Al BCC bulk with lattice constant a = 3.3 Å, force cubic cell
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Display lattice parameters and number of atoms
a, b, c = atoms.get_cell_lengths_and_angles()[:3]
alpha, beta, gamma = atoms.get_cell_lengths_and_angles()[3:]
print(f"Lattice parameters: a={a:6.2f} Å, b={b:6.2f} Å, c={c:6.2f} Å")
print(f"Crystal angles: 𝛼={alpha:6.2f}°, 𝛽={beta:6.2f}°, 𝛾={gamma:6.2f}°")
print(f"Number of atoms: {len(atoms)}\n")
print(f"Chemical formula: Al")
