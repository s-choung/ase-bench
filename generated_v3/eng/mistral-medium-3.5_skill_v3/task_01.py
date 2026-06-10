from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6)
supercell = atoms * (2, 2, 2)
supercell.calc = EMT()

print("Cell:", supercell.get_cell())
print("Number of atoms:", len(supercell))
