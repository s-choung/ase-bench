from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# Initialize H2 molecule with initial 1.2 Å bond length
atoms = Atoms('H2', positions=[[0, 0, 0], [1.2, 0, 0]], cell=[10, 10, 10], pbc=False)
atoms.calc = EMT()

# Calculate and print pre-constraint values
initial_bond = atoms.get_distance(0, 1)
initial_energy = atoms.get_potential_energy()
print(f"Before constraint: Bond length = {initial_bond:.3f} Å, Energy = {initial_energy:.4f} eV")

# Apply bond length constraint to fix H-H bond at 0.9 Å
atoms.set_constraint(FixBondLength(0, 1, bond_length=0.9))

# Relax system to enforce constraint
optimizer = BFGS(atoms, logfile=None)
optimizer.run(fmax=0.01)

# Calculate and print post-constraint values
final_bond = atoms.get_distance(0, 1)
final_energy = atoms.get_potential_energy()
print(f"After constraint:  Bond length = {final_bond:.3f} Å, Energy = {final_energy:.4f} eV")
