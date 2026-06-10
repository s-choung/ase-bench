from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Create H2 molecule with initial bond length ~0.74 Å
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

# Calculate initial bond length and energy
initial_bond_length = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()

print(f"Before constraint: Bond length = {initial_bond_length:.4f} Å, Energy = {initial_energy:.6f} eV")

# Apply FixBondLength constraint to fix bond length at 0.9 Å
constraint = FixBondLength(0, 1, 0.9)
h2.set_constraint([constraint])

# Optimize geometry with constraint
opt = BFGS(h2)
opt.run(fmax=0.01)

# Calculate final bond length and energy
final_bond_length = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()

print(f"After constraint:  Bond length = {final_bond_length:.4f} Å, Energy = {final_energy:.6f} eV")
