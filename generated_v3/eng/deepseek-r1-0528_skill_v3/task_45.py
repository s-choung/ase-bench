from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule with initial bond length 0.74 Å
atoms = Atoms('H2', positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.74]])
atoms.calc = EMT()
energy_before = atoms.get_potential_energy()
dist_before = atoms.get_distance(0, 1)
print(f"Before: Bond length = {dist_before:.5f} Å, Energy = {energy_before:.5f} eV")

# Apply constraint to maintain bond at 0.9 Å and move atoms to desired positions
atoms.positions[1] = [0.0, 0.0, 0.9]
c = FixBondLength(0, 1)
atoms.set_constraint(c)
energy_after = atoms.get_potential_energy()
dist_after = atoms.get_distance(0, 1)
print(f"After:  Bond length = {dist_after:.5f} Å, Energy = {energy_after:.5f} eV")
