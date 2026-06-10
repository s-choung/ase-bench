from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Create H2 molecule with initial bond length
atoms = Atoms('H2', positions=[(0, 0, 0), (0.74, 0, 0)])
atoms.calc = EMT()

# Energy and bond length before constraint
energy_before = atoms.get_potential_energy()
bond_length_before = atoms.get_distance(0, 1)

# Apply FixBondLength constraint
constraint = FixBondLength(0, 1, bondlength=0.9)
atoms.set_constraint(constraint)

# Optimize geometry after constraint
opt = BFGS(atoms, trajectory=None)
opt.run(fmax=0.05)

# Energy and bond length after constraint
energy_after = atoms.get_potential_energy()
bond_length_after = atoms.get_distance(0, 1)

print(f"Before: bond length = {bond_length_before:.3f} Å, energy = {energy_before:.3f} eV")
print(f"After:  bond length = {bond_length_after:.3f} Å, energy = {energy_after:.3f} eV")
