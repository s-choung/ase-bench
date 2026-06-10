from ase.build import bulk
from ase.calculators.emt import EMT

a = 2.95
c = a * 1.59
structure = bulk('Ti', crystalstructure='hcp', a=a, c=c)

print("Cell vectors:")
print(structure.cell)
print("\nAtomic positions:")
print(structure.positions)

calc = EMT()
structure.calc = calc
energy = structure.get_potential_energy()
print(f"\nPotential energy: {energy} eV")
