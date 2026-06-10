from ase import units
from ase.build import bulk
from ase.constraints import FixAtoms
from ase.md import NPTBerendsen
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()
atoms.set_constraint(FixAtoms(mask=[a.index < 26 for a in atoms]))

print('Initial volume:', atoms.get_volume())

dyn = NPTBerendsen(atoms, timestep=5 * units.fs,
                   taut=100 * units.fs, taup=1000 * units.fs,
                   temperature=300, pressure=1e5)
dyn.run(200)

print('Final volume:', atoms.get_volume())
print('Pressure:', atoms.get_stress()[0] / 1e5, 'bar')
