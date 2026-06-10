from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

v0 = atoms.get_volume()
pressure = 10 * 1e4 * units.bar  # 10 GPa to eV/Ang^3

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=500, pressure_au=pressure, taut=100*units.fs, taup=500*units.fs)
dyn.run(100)

print(f"Initial volume: {v0:.3f} Ang^3")
print(f"Final volume: {atoms.get_volume():.3f} Ang^3")
