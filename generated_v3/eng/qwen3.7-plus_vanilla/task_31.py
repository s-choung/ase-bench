from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs, GPa

atoms = bulk('Al', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

print("Initial volume:", atoms.get_volume())

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * fs,
    temperature_K=500,
    pressure_au=10 * GPa,
    taut=100 * fs,
    taup=100 * fs
)
dyn.run(100)

print("Final volume:", atoms.get_volume())
