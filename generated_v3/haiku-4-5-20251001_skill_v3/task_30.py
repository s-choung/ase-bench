from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((3, 3, 3))
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.4f} Ų")
print(f"Initial pressure: {atoms.get_stress()[0] / units.bar:.4f} bar")

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300, externalstress=1*units.bar,
                   taut=100*units.fs, taup=1000*units.fs)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.4f} Ų")
print(f"Final pressure: {atoms.get_stress()[0] / units.bar:.4f} bar")
