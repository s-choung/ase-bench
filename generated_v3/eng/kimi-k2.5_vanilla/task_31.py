from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.3f} Å³")

dyn = NPTBerendsen(atoms, timestep=1.0, temperature=500, pressure=10*GPa,
                   taut=100, taup=1000, compressibility=2.1)

dyn.run(100)

print(f"Final volume: {atoms.get_volume():.3f} Å³")
