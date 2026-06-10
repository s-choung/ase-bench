"""T1 Wiki: Create H2O molecule and print bond angle"""
from ase.build import molecule

atoms = molecule('H2O')
angle = atoms.get_angle(1, 0, 2)
print(f"H-O-H angle: {angle:.1f} degrees")
print(f"Positions:\n{atoms.get_positions()}")
print(f"Chemical formula: {atoms.get_chemical_formula()}")
