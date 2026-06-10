import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Cu", "fcc", a=3.615, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def pressure_bar(a):
    s = a.get_stress(voigt=False, include_ideal_gas=True)
    return -np.trace(s) / 3.0 / units.bar

print(f"Initial volume: {atoms.get_volume():.6f} A^3")
print(f"Initial pressure: {pressure_bar(atoms):.6f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility_au=7.14e-7 / units.bar,
    logfile=None,
)

dyn.run(200)

print(f"Final volume: {atoms.get_volume():.6f} A^3")
print(f"Final pressure: {pressure_bar(atoms):.6f} bar")
