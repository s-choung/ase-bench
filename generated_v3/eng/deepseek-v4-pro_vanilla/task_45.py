from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Initial H2 molecule with equilibrium bond length ~0.74 Å
atoms_before = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]])
atoms_before.calc = EMT()
energy_before = atoms_before.get_potential_energy()
bond_before = atoms_before.get_distance(0, 1)
print(f"Before constraint: bond length = {bond_before:.3f} Å, energy = {energy_before:.3f} eV")

# Set bond length to 0.9 Å and apply FixBondLength constraint
atoms_after = Atoms('H2', positions=[[0, 0, 0], [0.9, 0, 0]])
atoms_after.calc = EMT()
constraint = FixBondLength(0, 1)
atoms_after.set_constraint(constraint)
# The energy is evaluated at the fixed geometry; constraint is now active
energy_after = atoms_after.get_potential_energy()
bond_after = atoms_after.get_distance(0, 1)
print(f"After constraint:  bond length = {bond_after:.3f} Å, energy = {energy_after:.3f} eV")
