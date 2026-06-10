from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615).repeat(3)
atoms.calc = EMT()

vol_init = atoms.get_volume()
print(f"Initial volume: {vol_init:.3f} Å³")

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature=300*K, 
                   pressure=1.01325*units.bar, taut=100*units.fs, 
                   taup=1000*units.fs, trajectory='npt.traj')

for i, _ in enumerate(dyn.irun(200), 1):
    if i == 1 or i == 200:
        print(f"Step {i}: Volume = {atoms.get_volume():.3f} Å³, "
              f"Pressure = {dyn.get_pressure()/units.bar:.3f} bar")

vol_final = atoms.get_volume()
print(f"Final volume: {vol_final:.3f} Å³")
print(f"Volume change: {(vol_final-vol_init)/vol_init*100:.2f}%")
