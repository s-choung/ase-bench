from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Create H2 with an initial bond length different from 0.9 Å
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.8]])  # 0.8 Å initial
atoms.calc = EMT()

# Before constraint
bl_before = atoms.get_distance(0, 1)
e_before = atoms.get_potential_energy()
print(f"Before constraint: bond length = {bl_before:.3f} Å, energy = {e_before:.3f} eV")

# Apply FixBondLength constraint to keep H-H distance at 0.9 Å
atoms.set_constraint([FixBondLength(0, 1, 0.9)])

# Relax positions while respecting the constraint
opt = BFGS(atoms)
opt.run(fmax=0.05)

# After constraint (and relaxation)
bl_after = atoms.get_distance(0, 1)
e_after = atoms.get_potential_energy()
print(f"After constraint:  bond length = {bl_after:.3f} Å, energy = {e_after:.3f} eV")
