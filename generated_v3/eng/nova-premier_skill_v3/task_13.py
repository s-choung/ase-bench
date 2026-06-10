from ase.build import bulk
from ase.calculators.emt import EMT

a = bulk('Si', 'diamond', a=5.43)
sc = a * (3,3,3)
vol = sc.get_volume()
print(f"Atoms: {len(sc)}, Volume: {vol:.3f} Å³")
