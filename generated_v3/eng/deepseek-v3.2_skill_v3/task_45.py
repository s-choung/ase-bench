from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.units import kJ

# Create H2 molecule
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.0]])
atoms.calc = EMT()

# Calculate before constraint
energy_before = atoms.get_potential_energy()
bond_before = atoms.get_distance(0, 1)

print(f"Before constraint:")
print(f"  Bond length: {bond_before:.3f} Å")
print(f"  Energy: {energy_before:.6f} eV = {energy_before/kJ:.6f} kJ/mol")

# Apply FixBondLength constraint
constraint = FixBondLength(0, 1)
atoms.set_constraint([constraint])

# Set bond length to 0.9 Å
new_positions = [[0, 0, 0], [0, 0, 0.9]]
atoms.set_positions(new_positions)

# Calculate after constraint
energy_after = atoms.get_potential_energy()
bond_after = atoms.get_distance(0, 1)

print(f"\nAfter constraint (fixed at 0.9 Å):")
print(f"  Bond length: {bond_after:.3f} Å")
print(f"  Energy: {energy_after:.6f} eV = {energy_after/kJ:.6f} kJ/mol")
