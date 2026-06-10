from ase import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Initialize H2 molecule and calculator
atoms = molecule('H2')
atoms.calc = EMT()

# Before constraint
dist_before = atoms.get_distance(0, 1)
energy_before = atoms.get_potential_energy()
print(f"Before: Bond Length = {dist_before:.4f} Å, Energy = {energy_before:.4f} eV")

# Apply constraint to fix bond length at 0.9 Angstroms
# FixBondLength takes indices of the two atoms
atoms.set_constraint(FixBondLength(0, 1, 0.9))

# Adjust positions manually to 0.9A to reflect the constraint target
atoms.set_distance(0, 1, 0.9)

# After constraint
dist_after = atoms.get_distance(0, 1)
energy_after = atoms.get_potential_energy()
print(f"After: Bond Length = {dist_after:.4f} Å, Energy = {energy_after:.4f} eV")
