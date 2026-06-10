from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk("Al", "fcc", a=4.05, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500, force_temp=True)
Stationary(atoms)

pressure_gpa = 10.0
pressure_au = pressure_gpa / 160.21766208
compressibility_au = (1.0 / 76.0) * 160.21766208

print("Initial volume:", atoms.get_volume())

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=500,
    pressure_au=pressure_au,
    taut=100.0 * units.fs,
    taup=1000.0 * units.fs,
    compressibility_au=compressibility_au,
)

dyn.run(100)

print("Final volume:", atoms.get_volume())
