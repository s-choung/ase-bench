from ase.build import fcc111, octahedron
from ase.calculators.emt import EMT
from ase.io import write

a = 3.61
n = 5
cu = octahedron(size=n, symbol='Cu', a=a)
cu.calc = EMT()

print(len(cu))
print(cu.get_positions())

write('cu_octahedron.xyz', cu)
