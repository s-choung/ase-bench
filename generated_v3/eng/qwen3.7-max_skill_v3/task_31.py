from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.2f} Ang^3")

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

pressure_eV_A3 = 10 * units.GPa

dyn = NPTBerendsen(
    atoms,
    timestep=2 * units.fs,
    temperature_K=500,
    taut=100 * units.fs,
    pressure=pressure_eV_A3,
    taup=1000 * units.fs,
    compressibility_au=1.4e-5 / units.bar
)

dyn.run(100)

print(f"Final volume: {atoms.get_volume():.2f} Ang^3")
