from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial volume: {atoms.get_volume():.2f} Å³")
print(f"Initial pressure: {atoms.get_isotropic_pressure():.2f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    externalstress=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs
)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.2f} Å³")
print(f"Final pressure: {atoms.get_isotropic_pressure():.2f} bar")
