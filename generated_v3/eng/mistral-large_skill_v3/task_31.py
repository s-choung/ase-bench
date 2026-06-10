from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.calculators.emt import EMT

atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

pressure_GPa = 10.0
pressure_eV_A3 = pressure_GPa * 1e9 * units.Pa / (units.eV / units.Angstrom**3)

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=500,
                   pressure_au=pressure_eV_A3, taut=100*units.fs, taup=1000*units.fs,
                   compressibility_au=4.57e-5 / (units.eV / units.Angstrom**3))

print(f"Initial volume: {atoms.get_volume():.2f} Å³")
dyn.run(100)
print(f"Final volume: {atoms.get_volume():.2f} Å³")
