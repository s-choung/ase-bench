from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615).repeat([3, 3, 3])
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

initial_volume = atoms.get_volume()
stress0 = atoms.get_stress(include_ideal_gas=True)
P0 = -(stress0[0] + stress0[1] + stress0[2]) / 3

dyn = NPTBerendsen(atoms, 5 * units.fs, 300 * units.kB,
                   1.0 * units.bar, taut=100 * units.fs, taup=1000 * units.fs)
dyn.run(200)

final_volume = atoms.get_volume()
stress1 = atoms.get_stress(include_ideal_gas=True)
P1 = -(stress1[0] + stress1[1] + stress1[2]) / 3

p0 = P0 * units.eV / units.Ang**3 / units.bar
p1 = P1 * units.eV / units.Ang**3 / units.bar

print(f'Initial volume: {initial_volume:.2f} Ang^3')
print(f'Final volume: {final_volume:.2f} Ang^3')
print(f'Initial pressure: {p0:.4f} bar')
print(f'Final pressure: {p1:.4f} bar')
