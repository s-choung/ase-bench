from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

print("Cell vectors (Å):")
print(atoms.cell[:])
print(f"\nCell lengths and angles: {atoms.cell.cellpar()}")
print(f"Number of atoms: {len(atoms)}")
print(f"Volume: {atoms.get_volume():.3f} Å³")
print(f"Potential energy: {atoms.get_potential_energy():.4f} eV")
