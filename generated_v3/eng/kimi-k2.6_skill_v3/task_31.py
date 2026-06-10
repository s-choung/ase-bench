from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc', a=4.05)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

pressure = 10e4 * units.bar  # 10 GPa -> eV/Å^3

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=500,
                   pressure=pressure, taut=100*units.fs, taup=500*units.fs,
                   compressibility=1.5e-6/units.bar)

print(f"Initial volume: {atoms.get_volume():.3f} Å³")
dyn.run(100)
print(f"Final volume: {atoms.get_volume():.3f} Å³")
