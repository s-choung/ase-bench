from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Create an H2 molecule
atoms = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.74)])

# Calculate energy before constraint
atoms.calc = EMT()
energy_before = atoms.get_potential_energy()
bond_length_before = atoms.get_distances()[0]
print(f"Before constraint:")
print(f"  Bond length: {bond_length_before:.3f} Å")
print(f"  Energy: {energy_before:.3f} eV")

# Apply constraint
constraint = FixBondLength(0, 1, 0.9)
atoms.set_constraint(constraint)

# Calculate energy after constraint
energy_after = atoms.get_potential_energy()
bond_length_after = atoms.get_distances()[0]
print(f"\nAfter constraint:")
print(f"  Bond length: {bond_length_after:.3f} Å")
print(f"  Energy: {energy_after:.3f} eV")
