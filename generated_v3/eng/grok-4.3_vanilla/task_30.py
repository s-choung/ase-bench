from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
atoms = bulk('Cu', cubic=True)*(3,3,3)
atoms.calc = EMT()
print(atoms.get_volume(), atoms.get_isotropic_pressure(atoms.get_stress()))
NPTBerendsen(atoms, 5*units.fs, 300, 1*units.bar, 100*units.fs, 1000*units.fs).run(200)
print(atoms.get_volume(), atoms.get_isotropic_pressure(atoms.get_stress()))
