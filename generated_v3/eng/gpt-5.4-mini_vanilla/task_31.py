from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T = 500.0
P_GPa = 10.0
P = P_GPa / 160.21766208  # eV/Ang^3

print("Initial volume:", atoms.get_volume())

MaxwellBoltzmannDistribution(atoms, temperature_K=T)
Stationary(atoms)
ZeroRotation(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=T,
    pressure_au=P,
    taut=100.0 * units.fs,
    taup=1000.0 * units.fs,
    compressibility_au=1.0 / 76.0,
)

dyn.run(100)

print("Final volume:", atoms.get_volume())
