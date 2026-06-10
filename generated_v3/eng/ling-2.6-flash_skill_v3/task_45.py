from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# H2 molecule
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.9]])
atoms.calc = EMT()

# Before constraint
print(f"Before: bond length = {atoms.get_distance(0, 1):.3f} Å, energy = {atoms.get_potential_energy():.3f} eV")

# Apply FixBondLength at 0.9 Å
atoms.set_constraint(FixBondLength(atoms, 0, 1, value=0.9))

# After constraint
print(f"After:  bond length = {atoms.get_distance(0, 1):.3f} Å, energy = {atoms.get_potential_energy():.3f} eV")
