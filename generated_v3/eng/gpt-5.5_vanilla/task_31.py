from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.md.nptberendsen import NPTBerendsen

atoms = bulk("Al", "fcc", a=4.05, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

temperature = 500.0
pressure_GPa = 10.0
pressure_au = pressure_GPa * units.GPa
compressibility_au = (1.0 / 76.0) / units.GPa

MaxwellBoltzmannDistribution(atoms, temperature_K=temperature)
Stationary(atoms)
ZeroRotation(atoms)

print(f"Pressure: {pressure_GPa} GPa = {pressure_au:.8f} eV/Ang^3")
print(f"Initial volume: {atoms.get_volume():.6f} Ang^3")

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=temperature,
    pressure_au=pressure_au,
    taut=100.0 * units.fs,
    taup=1000.0 * units.fs,
    compressibility_au=compressibility_au,
    logfile=None,
)

dyn.run(100)

print(f"Final volume: {atoms.get_volume():.6f} Ang^3")
