from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Create H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]])
h2.calc = EMT()

# Before constraint
e_before = h2.get_potential_energy()
d_before = h2.get_distance(0, 1)
print(f"Before: bond={d_before:.3f} Å, energy={e_before:.3f} eV")

# Apply constraint and optimize
h2.set_constraint(FixBondLength(0, 1))
h2.positions[1, 0] = 0.9  # Set initial bond length
BFGS(h2).run(fmax=0.01)

# After constraint
e_after = h2.get_potential_energy()
d_after = h2.get_distance(0, 1)
print(f"After: bond={d_after:.3f} Å, energy={e_after:.3f} eV")
