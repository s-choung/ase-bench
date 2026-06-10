from ase import units
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
pressure = 10 * units.GPa * (units.Ang**3 / units.eV)

print(f"Initial volume: {atoms.get_volume():.3f} Ang^3")

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
dynamics = NPTBerendsen(atoms, 5*units.fs, 500, pressure, taut=100*units.fs, taup=1000*units.fs)
dynamics.run(100)

print(f"Final volume: {atoms.get_volume():.3f} Ang^3")
