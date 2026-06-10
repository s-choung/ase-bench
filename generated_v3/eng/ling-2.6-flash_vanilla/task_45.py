from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import QuasiNewton

# Create H2 molecule with initial bond length 1.0 Angstrom
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.0]])
atoms.calc = EMT()

# Calculate and print energy before constraint
energy_before = atoms.get_potential_energy()
bond_before = atoms.get_distance(0, 1)
print(f"Before FixBondLength: bond = {bond_before:.3f} Å, energy = {energy_before:.3f} eV")

# Apply FixBondLength constraint at 0.9 Angstrom
atoms.set_constraint(FixBondLength(atoms, [0, 1], 0.9))

# Optimize geometry with the constraint
opt = QuasiNewton(atoms)
opt.run(fmax=0.01)

# Calculate and print energy after constraint
energy_after = atoms.get_potential_energy()
bond_after = atoms.get_distance(0, 1)
print(f"After FixBondLength:  bond = {bond_after:.3f} Å, energy = {energy_after:.3f} eV")
