from ase.build import bulk
from ase.calculators.emt import EMT

si = bulk('Si', 'diamond', a=5.43)
si = si.repeat((3, 3, 3))
si.calc = EMT()
print(f"Number of atoms: {len(si)}")
print(f"Cell volume: {si.get_volume():.3f} Å^3")
