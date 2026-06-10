from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Al", "fcc", a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

temperature = 500.0
pressure_gpa = 10.0
pressure_au = pressure_gpa / 160.21766208
bulk_modulus_al_gpa = 76.0
compressibility_au = 1.0 / (bulk_modulus_al_gpa / 160.21766208)

MaxwellBoltzmannDistribution(atoms, temperature_K=temperature)
Stationary(atoms)

print("Initial volume:", atoms.get_volume())

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=temperature,
    taut=100.0 * units.fs,
    pressure_au=pressure_au,
    taup=1000.0 * units.fs,
    compressibility_au=compressibility_au,
)

dyn.run(100)

print("Final volume:", atoms.get_volume())
