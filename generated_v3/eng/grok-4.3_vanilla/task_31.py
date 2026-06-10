from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
atoms = bulk('Al', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
print(atoms.get_volume())
dyn = NPTBerendsen(atoms, 5 * units.fs, 500, 10 * units.GPa, 25 * units.fs, 25 * units.fs)
dyn.run(100)
print(atoms.get_volume())
