from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 at equilibrium (~0.74 Å)
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

print("=== Before applying FixBondLength ===")
print(f"Bond length: {h2.get_distance(0, 1):.4f} Å")
print(f"Energy:      {h2.get_potential_energy():.6f} eV")

# Set bond length to 0.9 Å and apply constraint
h2.set_positions([[0, 0, 0], [0, 0, 0.9]])
h2.set_constraint(FixBondLength(0, 1))

print("\n=== After applying FixBondLength (0.9 Å) ===")
print(f"Bond length: {h2.get_distance(0, 1):.4f} Å")
print(f"Energy:      {h2.get_potential_energy():.6f} eV")

# Verify constraint holds during a short optimization
from ase.optimize import BFGS
opt = BFGS(h2)
opt.run(fmax=0.01, steps=10)

print("\n=== After BFGS optimization (bond constrained) ===")
print(f"Bond length: {h2.get_distance(0, 1):.4f} Å")
print(f"Energy:      {h2.get_potential_energy():.6f} eV")
