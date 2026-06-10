from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Create H2 molecule with initial bond length of 0.7 Å
h2 = Atoms('H2', positions=[[0, 0, 0], [0.7, 0, 0]])
h2.calc = EMT()

# Calculate energy and bond length before constraint
bond_length_before = h2.get_distance(0, 1)
energy_before = h2.get_potential_energy()

print(f"Before constraint: bond length = {bond_length_before:.4f} Å, energy = {energy_before:.6f} eV")

# Apply FixBondLength constraint to fix bond length at 0.9 Å
constraint = FixBondLength(0, 1, 0.9)
h2.set_constraint(constraint)

# Optimize geometry with constraint
opt = BFGS(h2)
opt.run(fmax=0.01)

# Calculate energy and bond length after constraint
bond_length_after = h2.get_distance(0, 1)
energy_after = h2.get_potential_energy()

print(f"After constraint: bond length = {bond_length_after:.4f} Å, energy = {energy_after:.6f} eV")
