from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.md import MDLogger
from ase.io import Trajectory
from ase.md.npt import Inhomogeneous_NPTBerendsen
from ase.md.nptberendsen import NPTBerendsen
from ase.md import VelocityVerlet
from ase.md.nptberendsen import NPTBerendsen
from ase.md.npt import NPT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.npt import NPT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.npt import NPT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.npt import NPT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.npt import NPT
from ase.md.nptberendsen import NPT
from ase.md.nptberendsen import NPTBerendsen

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    taut=100 * units.fs,
    pressure_au=1 * units.bar,
    taup=1000 * units.fs,
    compressibility_au=1.0 / units.GPa,
)

print("Initial volume (A^3):", atoms.get_volume())
print("Initial pressure (bar):", atoms.get_pressure() / units.bar)

for _ in range(200):
    dyn.run(1)

print("Final volume (A^3):", atoms.get_volume())
print("Final pressure (bar):", atoms.get_pressure() / units.bar)
