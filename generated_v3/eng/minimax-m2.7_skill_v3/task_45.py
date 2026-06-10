from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.9)])
h2.calc = EMT()

dist_before = h2.get_distance(0, 1)
energy_before = h2.get_potential_energy()

print(f"Before constraint:")
print(f"  Bond length: {dist_before:.4f} Å")
print(f"  Energy: {energy_before:.4f} eV")

h2.set_constraint(FixBondLength(0, 1))

dist_after = h2.get_distance(0, 1)
energy_after = h2.get_potential_energy()

print(f"\nAfter constraint:")
print(f"  Bond length: {dist_after:.4f} Å")
print(f"  Energy: {energy_after:.4f} eV")
