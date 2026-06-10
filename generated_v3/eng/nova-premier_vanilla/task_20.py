from ase.build import nanotube
from ase.calculators.emt import EMT

tube = nanotube(6, 6, length=4, bond=1.42)
tube.calc = EMT()
print(f"Atoms: {len(tube)}")
print(f"Cell: {tube.cell.cellpar()}")
