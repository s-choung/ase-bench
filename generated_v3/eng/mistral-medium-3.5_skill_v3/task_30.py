from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300,
                   pressure=1*units.bar, taut=100*units.fs, taup=1000*units.fs)
print(f"Initial volume: {atoms.get_volume():.2f} Å^3")
dyn.run(200)
print(f"Final volume: {atoms.get_volume():.2f} Å^3, pressure: {atoms.calc.results['pressure']:.2f} eV/Å^3")
