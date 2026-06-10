from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators import EMT

h2 = molecule('h2')
calc = EMT()
h2.calc = calc

bond_length_before = h2.get_distance(0, 1)
energy_before = h2.get_potential_energy()

constraint = FixBondLength(0, 1, 0.9)
h2.set_constraint(constraint)

bond_length_after = h2.get_distance(0, 1)
energy_after = h2.get_potential_energy()

print(f"Bond length before: {bond_length_before:.4f} Angstroms")
print(f"Energy before: {energy_before:.4f} eV")
print(f"Bond length after: {bond_length_after:.4f} Angstroms")
print(f"Energy after: {energy_after:.4f} eV")
