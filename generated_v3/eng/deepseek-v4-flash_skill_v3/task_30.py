from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.3f} A^3")
stress = atoms.get_stress()
p0 = -sum(stress[:3]) / 3
print(f"Initial pressure: {p0:.6e} eV/A^3")

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300,
                   taut=100*units.fs, taup=1000*units.fs,
                   pressure=1*units.bar, compressibility=4.5e-5)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.3f} A^3")
stress = atoms.get_stress()
p1 = -sum(stress[:3]) / 3
print(f"Final pressure: {p1:.6e} eV/A^3")
