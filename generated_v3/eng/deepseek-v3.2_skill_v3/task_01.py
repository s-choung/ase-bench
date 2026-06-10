from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6)
supercell = atoms.repeat((2, 2, 2))
supercell.calc = EMT()

print(f"Cell vectors:\n{supercell.cell}")
print(f"Number of atoms: {len(supercell)}")
