from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((3,3,3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

def get_pressure(a):
    s = a.get_stress(include_ideal_gas=True, voigt=False)
    return -np.trace(s)/3.0 / units.bar

print(f"Initial volume: {atoms.get_volume():.4f} A^3")
print(f"Initial pressure: {get_pressure(atoms):.4f} bar")

dyn = NPTBerendsen(atoms, timestep=5.0*units.fs, temperature_K=300,
                   pressure_au=1.0*units.bar,
                   taut=100*units.fs, taup=1000*units.fs,
                   compressibility_au=4.57e-5/units.bar)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.4f} A^3")
print(f"Final pressure: {get_pressure(atoms):.4f} bar")
