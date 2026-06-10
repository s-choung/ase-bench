from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units
from ase.io import write

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

T = 300
P = 1.0e5  # Pa

print(f"Initial volume: {atoms.get_volume():.6f} A^3")
print(f"Initial pressure: {atoms.get_pressure():.6f} bar")

MaxwellBoltzmannDistribution(atoms, temperature_K=T)
Stationary(atoms)
ZeroRotation(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=T,
    taut=100 * units.fs,
    pressure_au=P / units.Pascal,
    taup=1000 * units.fs,
    compressibility_au=1.0 / (140e9 / units.Pascal),
)

dyn.run(200)

print(f"Final volume: {atoms.get_volume():.6f} A^3")
print(f"Final pressure: {atoms.get_pressure():.6f} bar")
