from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

v0 = atoms.get_volume()
p0 = atoms.get_pressure()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)

dyn.run(200)

v1 = atoms.get_volume()
p1 = atoms.get_pressure()

print(v0, p0)
print(v1, p1)
