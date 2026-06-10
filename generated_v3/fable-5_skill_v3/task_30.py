import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def get_pressure(a):
    stress = a.get_stress(voigt=True)
    return -stress[:3].mean() / units.bar

print(f"Initial volume: {atoms.get_volume():.3f} A^3")
print(f"Initial pressure: {get_pressure(atoms):.2f} bar")

dyn = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=300,
                   pressure_au=1.0 * units.bar,
                   taut=100 * units.fs, taup=1000 * units.fs,
                   compressibility_au=7e-7 / units.bar)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.3f} A^3")
print(f"Final pressure: {get_pressure(atoms):.2f} bar")
print(f"Final temperature: {atoms.get_temperature():.1f} K")
