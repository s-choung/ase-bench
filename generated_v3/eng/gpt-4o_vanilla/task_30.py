from ase.build import bulk
from ase import units
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
cu.calc = EMT()

dyn = NPTBerendsen(cu, 
                   timestep=5 * units.fs, 
                   temperature=300 * units.kB, 
                   pressure=1.01325, 
                   taut=100 * units.fs, 
                   taup=1000 * units.fs)

print(f"Initial volume: {cu.get_volume()} Å^3, Initial pressure: {cu.get_pressure()} bar")

dyn.run(200)

print(f"Final volume: {cu.get_volume()} Å^3, Final pressure: {cu.get_pressure()} bar")
