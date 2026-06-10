from ase.build import fcc_111
from ase.io import write, read
from ase.calculators.emt import EMT
from ase.calculators.lj import lennardjones

atoms = fcc_111('Au', size=2, symbol='Au')

atoms.calc = EMT()
write('Au_fcc.xyz', atoms)

atoms2 = read('Au_fcc.xyz')

print(atoms2.get_atomic_numbers())
print(atoms2.get_positions())
