from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create an H2 molecule
atoms = Atoms('H2', positions=[(0, 0, 0), (1.0, 0, 0)])

# Print initial bond length and energy
calc = EMT()
atoms.calc = calc
bond_length_initial = atoms.get_distance(0, 1)
energy_initial = atoms.get_potential_energy()
print(f"Initial bond length: {bond_length_initial:.3f} Å")
print(f"Initial energy: {energy_initial:.6f} eV")

# Apply FixBondLength constraint with a target bond length of 0.9 Å
atoms.constraints = FixBondLength(0, 1, 0.9)

# Recalculate energy with the constraint applied
atoms.calc = calc
energy_final = atoms.get_potential_energy()
bond_length_final = atoms.get_distance(0, 1)
print(f"Final bond length: {bond_length_final:.3f} Å")
print(f"Final energy: {energy_final:.6f} eV")
