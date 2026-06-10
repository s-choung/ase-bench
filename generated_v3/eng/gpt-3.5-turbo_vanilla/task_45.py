from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import QuasiNewton

# Create H2 molecule
h2 = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.74)])

# Calculate energy before applying constraint
h2.set_calculator(EMT())
energy_before = h2.get_potential_energy()
bond_length_before = h2.get_distance(0, 1)

# Apply FixBondLength constraint to fix bond length at 0.9 angstroms
constraint = FixBondLength(0, 1)
h2.set_constraint(constraint)

# Calculate energy after applying constraint
energy_after = h2.get_potential_energy()
bond_length_after = h2.get_distance(0, 1)

print("Before constraint - Bond Length: {:.2f} Angstroms, Energy: {:.2f} eV".format(bond_length_before, energy_before))
print("After constraint - Bond Length: {:.2f} Angstroms, Energy: {:.2f} eV".format(bond_length_after, energy_after))
