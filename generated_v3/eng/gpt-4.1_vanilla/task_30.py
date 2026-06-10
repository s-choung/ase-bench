from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615).repeat((3,3,3))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

timestep = 5 * units.fs
taut = 100 * units.fs
taup = 1000 * units.fs

initial_vol = atoms.get_volume()
dyn = NPTBerendsen(atoms, timestep, temperature_K=300, externalstress=1.01325, taut=taut, taup=taup)  # 1 bar = 1.01325e5 Pa (use 1.01325 in ASE units)
print(f'Initial cell volume: {initial_vol:.2f} Å^3')
print(f'Initial pressure: {atoms.get_pressure():.2f} bar')

dyn.run(200)

final_vol = atoms.get_volume()
# ASE get_pressure is in bar if units not changed
print(f'Final cell volume: {final_vol:.2f} Å^3')
print(f'Final pressure: {atoms.get_pressure():.2f} bar')
