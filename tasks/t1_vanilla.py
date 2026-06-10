"""T1 Vanilla: Create H2O molecule and print bond angle"""
from ase.data.molecules import molecule

atoms = molecule('H2O')
angle = atoms.get_angle(0, 1, 2)
print(f"H-O-H angle: {angle:.1f} degrees")
print(f"Positions:\n{atoms.get_positions()}")
