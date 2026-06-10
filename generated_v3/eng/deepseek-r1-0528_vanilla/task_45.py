from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule with initial bond length of 0.74 Å
atoms = Atoms('HH', positions=[[0, 0, 0], [0.74, 0, 0]])
atoms.calc = EMT()

# Before constraint
energy_pre = atoms.get_potential_energy()
bond_length_pre = atoms.get_distance(0, 1)
print(f"Before: Bond Length = {bond_length_pre:.4f} Å, Energy = {energy_pre:.6f} eV")

# Apply constraint to fix bond length at 0.9 Å
constraint = FixBondLength(0, 1, length=0.9)
atoms.set_constraint(constraint)
positions = atoms.get_positions()
constraint.adjust_positions(atoms.positions, positions)
atoms.set_positions(positions)

# After constraint
energy_post = atoms.get_potential_energy()
bond_length_post = atoms.get_distance(0, 1)
print(f"After: Bond Length = {bond_length_post:.4f} Å, Energy = {energy_post:.6f} eV")
