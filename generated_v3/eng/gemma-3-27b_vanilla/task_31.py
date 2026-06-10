from ase.build import fcc111
from ase.md.verlet import VelocityVerlet
from ase.md.langevin import Langevin
from ase.md.berendsen import NPTBerendsen
from ase import units

al = fcc111('Al', size=(2, 2, 2), vacuum=1.0)

calculator = EMT()
al.calc = calculator

nv = NPTBerendsen(al, 500 * units.kB, pressure=10.0 * units.GPa,
                   length=100, friction=0.02)

initial_volume = al.get_volume()
print(f"Initial volume: {initial_volume:.3f} Ang^3")

nv.run(100)

final_volume = al.get_volume()
print(f"Final volume: {final_volume:.3f} Ang^3")
