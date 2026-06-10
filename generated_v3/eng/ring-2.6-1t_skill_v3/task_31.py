from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

press_eV = 10.0e9 / (1.0e-10**-3 / 1.602176634e-19)
# 10 GPa in eV/A^3:
press_ev_a3 = 10.0 / 160.2176634

dyn = NPTBerendsen(atoms, timestep=1.0 * units.fs, temperature_K=500,
                   pressure_=press_ev_a3 * units.bar,
                   taut=20 * units.fs, taup=100 * units.fs)

Vol_i = atoms.get_volume()

dyn.run(steps=100)

Vol_f = atoms.get_volume()

print(f"Initial volume = {Vol_i:.3f} Ang^3")
print(f"Final volume   = {Vol_f:.3f} Ang^3")
