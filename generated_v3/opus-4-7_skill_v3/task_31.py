from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

print(f"Initial volume: {atoms.get_volume():.4f} Ang^3")

pressure_au = 10.0 * units.GPa

dyn = NPTBerendsen(atoms, timestep=2*units.fs, temperature_K=500,
                   pressure_au=pressure_au, compressibility_au=1e-2/units.GPa)
dyn.run(100)

print(f"Final volume: {atoms.get_volume():.4f} Ang^3")
print(f"Final temperature: {atoms.get_temperature():.2f} K")
