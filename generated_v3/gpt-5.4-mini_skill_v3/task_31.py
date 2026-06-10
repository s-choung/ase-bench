import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

v0 = atoms.get_volume()
print(f"Initial volume: {v0:.6f} Å^3")

pressure = 10.0 * 1e9 / 1.602176634e11  # GPa -> eV/Å^3

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=500,
    pressure_au=pressure,
    taut=100.0 * units.fs,
    taup=1000.0 * units.fs,
    compressibility_au=1.0 / 76.0,
)

dyn.run(100)

v1 = atoms.get_volume()
print(f"Final volume: {v1:.6f} Å^3")
