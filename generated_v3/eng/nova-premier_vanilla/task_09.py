from ase import Atoms
from ase.calculators.emt import EMT
from ase.io.vasp import write_vasp, read_vasp

# Create Cu FCC bulk
atoms = Atoms('Cu', positions=[(0, 0, 0)], cell=[3.6, 3.6, 3.6], pbc=True)
atoms *= (2, 2, 2)
calc = EMT()
atoms.calc = calc

# Save to POSCAR
write_vasp('POSCAR', atoms, direct=True, vasp5=True)

# Read from POSCAR
atoms2 = read_vasp('POSCAR')
print(f"Atoms: {len(atoms2)}")
print(f"Cell: {atoms2.cell.cellpar()}")
