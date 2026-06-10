from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.61) * (2, 2, 2)
atoms.calc = EMT()
d = atoms.get_distances(0, range(len(atoms)), mic=True)
print(f"Min: {d[d>0].min():.3f} Å")
print(f"Max: {d.max():.3f} Å")
