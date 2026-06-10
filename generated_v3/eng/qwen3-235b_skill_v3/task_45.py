from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule
atoms = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]])
atoms.calc = EMT()

# Before constraint
energy_before = atoms.get_potential_energy()
bond_length_before = atoms.get_distances(0, 1)[0]
print(f"Before: Bond length = {bond_length_before:.3f} Å, Energy = {energy_before:.3f} eV")

# Apply FixBondLength constraint
c = FixBondLength(0, 1, bondlength=0.9)
atoms.set_constraint(c)

# Calculate energy after constraint
energy_after = atoms.get_potential_energy()
bond_length_after = atoms.get_distances(0, 1)[0]
print(f"After: Bond length = {bond_length_after:.3f} Å, Energy = {energy_after:.3f} eV")
