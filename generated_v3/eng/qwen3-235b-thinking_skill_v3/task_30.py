from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
import numpy as np

atoms = bulk('Cu', 'fcc') * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

vol0 = atoms.get_volume()
ke0 = atoms.get_kinetic_energy()
pk0 = 2 * ke0 / (3 * vol0)
ppot0 = -np.trace(atoms.get_stress(voigt=False)) / 3.0
p0 = pk0 + ppot0

dyn = NPTBerendsen(atoms, 5*units.fs, temperature_K=300, pressure=1*units.bar, taut=100*units.fs, taup=1000*units.fs)
for _ in range(200):
    dyn.run(1)

vol1 = atoms.get_volume()
ke1 = atoms.get_kinetic_energy()
pk1 = 2 * ke1 / (3 * vol1)
ppot1 = -np.trace(atoms.get_stress(voigt=False)) / 3.0
p1 = pk1 + ppot1

print(f"Initial volume: {vol0:.2f} Å³, pressure: {p0:.6f} eV/Å³")
print(f"Final volume: {vol1:.2f} Å³, pressure: {p1:.6f} eV/Å³")
