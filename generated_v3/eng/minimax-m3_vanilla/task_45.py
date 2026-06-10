from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# H2 molecule with initial bond length 1.5 Å
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.5]])
atoms.calc = EMT()

# Before applying constraint
d_before = atoms.get_distance(0, 1)
e_before = atoms.get_potential_energy()
print(f"Before: bond length = {d_before:.4f} Å, energy = {e_before:.4f} eV")

# Apply FixBondLength constraint at 0.9 Å
atoms.set_constraint(FixBondLength(0, 1, bond=0.9))

# Set positions to satisfy the constrained bond length
atoms.set_positions([[0, 0, 0], [0, 0, 0.9]])

# After applying constraint
d_after = atoms.get_distance(0, 1)
e_after = atoms.get_potential_energy()
print(f"After:  bond length = {d_after:.4f} Å, energy = {e_after:.4f} eV")
