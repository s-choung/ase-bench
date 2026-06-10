from ase.build import molecule
from ase.calculators.lj import LennardJones
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Initialize H2 molecule with LJ calculator
h2 = molecule('H2')
h2.calc = LennardJones()

# Unconstrained relaxation
opt_unconstrained = BFGS(h2, logfile=None)
opt_unconstrained.run(fmax=0.01)
bond_before = h2.get_distance(0, 1)
energy_before = h2.get_potential_energy()
print(f"Before constraint: Bond length = {bond_before:.3f} Å, Energy = {energy_before:.4f} eV")

# Apply FixBondLength constraint to lock bond at 0.9 Å
h2.set_constraint(FixBondLength(0, 1, fixedlength=0.9))

# Relax with constraint active
opt_constrained = BFGS(h2, logfile=None)
opt_constrained.run(fmax=0.01)
bond_after = h2.get_distance(0, 1)
energy_after = h2.get_potential_energy()
print(f"After constraint:  Bond length = {bond_after:.3f} Å, Energy = {energy_after:.4f} eV")
