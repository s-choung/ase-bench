from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Create H2 molecule
h2 = Atoms('H2', positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.7]], calculator=EMT())

# Print initial bond length and energy
initial_bond_length = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()
print(f"Before constraint - Bond length: {initial_bond_length:.3f} Å, Energy: {initial_energy:.3f} eV")

# Apply FixBondLength constraint (for atoms 0 and 1, fix at 0.9 Å)
h2.set_constraint(FixBondLength(0, 1, 0.9))

# Optimize (though constraint will prevent bond length change)
opt = BFGS(h2)
opt.run(fmax=0.01)

# Print final bond length and energy
final_bond_length = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()
print(f"After constraint - Bond length: {final_bond_length:.3f} Å, Energy: {final_energy:.3f} eV")
