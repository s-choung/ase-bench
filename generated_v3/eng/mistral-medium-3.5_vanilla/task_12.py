from ase.lattice.hexagonal import Hexagonal, HexagonalFactory
from ase.spacegroup import crystal

a = 2.95
c = a * 1.59
ti = Hexagonal(symbol='Ti', latticeconstant={'a': a, 'c': c})
print("Cell vectors:\n", ti.get_cell())
print("Atomic positions:\n", ti.get_positions())
