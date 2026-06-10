from ase.build import bulk
from ase.io import read, write
from ase.calculators.emt import EMT

# Create Cu FCC bulk structure, attach built-in EMT calculator
atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()

# Save structure to VASP POSCAR format
write('POSCAR', atoms)

# Read POSCAR back into ASE Atoms object
read_atoms = read('POSCAR')

# Print required metrics
print(f"Number of atoms: {len(read_atoms)}")
a, b, c, alpha, beta, gamma = read_atoms.cell.cellpar()
print(f"Cell parameters: a={a:.3f} Å, b={b:.3f} Å, c={c:.3f} Å, alpha={alpha:.1f}°, beta={beta:.1f}°, gamma={gamma:.1f}°")
