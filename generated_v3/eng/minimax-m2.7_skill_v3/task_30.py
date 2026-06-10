from ase import Atoms, units
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.62).repeat((3, 3, 3))
atoms.calc = EMT()

vol_init = atoms.get_volume()
p_init = atoms.get_pressure()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_Pa=1e5,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility=None,
    timeconstant=True,
    rng=None
)
dyn.run(200)

vol_final = atoms.get_volume()
p_final = atoms.get_pressure()

print(f"Initial volume: {vol_init:.2f} Å³")
print(f"Final volume:   {vol_final:.2f} Å³")
print(f"Initial pressure: {p_init:.2f} bar")
print(f"Final pressure:   {p_final:.2f} bar")
