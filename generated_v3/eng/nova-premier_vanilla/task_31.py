from ase import build, units
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT

al = build.bulk("Al", "fcc", a=4.05, cubic=True).repeat((2, 2, 2))
al.calc = EMT()
dyn = NPTBerendsen(al, 1*units.fs, 500, 10*1e9/units.Pascal, compressibility=75*units.GPa, traj='al.traj')
print("Initial volume:", al.get_volume())
dyn.run(100)
print("Final volume:", al.get_volume())
