from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]])
h2.calc = EMT()

# Print initial bond length and energy
initial_length = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()
print(f"Initial bond length: {initial_length:.4f} Å")
print(f"Initial energy: {initial_energy:.4f} eV")

# Apply FixBondLength constraint
h2.set_constraint(FixBondLength(0, 1))

# Set bond length to 0.9 Å by moving second atom
h2.positions[1] = [0.9, 0, 0]

# Print bond length and energy after constraint
final_length = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()
print(f"Final bond length: {final_length:.4f} Å")
print(f"Final energy: {final_energy:.4f} eV")
