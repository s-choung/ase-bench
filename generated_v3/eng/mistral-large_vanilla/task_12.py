from ase.lattice.hexagonal import HexagonalClosedPacked
from ase.calculators.emt import EMT

a = 2.95
c_a = 1.59
hcp = HexagonalClosedPacked(size=(2, 2, 2), symbol='Ti', latticeconstant={'a': a, 'c/a': c_a})

print("Cell vectors:")
print(hcp.cell)
print("\nAtomic positions:")
for atom in hcp:
    print(atom.position)
