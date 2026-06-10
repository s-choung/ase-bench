from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule with initial bond length ~0.74 Å
h2 = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.74)])
h2.calc = EMT()

# Before constraint
bond_before = h2.get_distance(0, 1)
energy_before = h2.get_potential_energy()
print(f"Before: bond length = {bond_before:.4f} Å, energy = {energy_before:.6f} eV")

# Apply FixBondLength constraint at 0.9 Å
constraint = FixBondLength(0, 1, length=0.9)
h2.set_constraint(constraint)

# After constraint
bond_after = h2.get_distance(0, 1)
energy_after = h2.get_potential_energy()
print(f"After:  bond length = {bond_after:.4f} Å, energy = {energy_after:.6f} eV")
