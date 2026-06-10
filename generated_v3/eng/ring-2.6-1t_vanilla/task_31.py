import numpy as np
from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.npt import NPTBerendsen

# FCC Al, 2x2x2 supercell
al = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
al.calc = EMT()

# target pressure 10 GPa → eV/Å³
press_pa = 10 * units.GPa                # 1e10 Pa
press_ev = press_pa / (units.eV / units.Ang**3)   # ≈ 0.0624 eV/Å³

print('initial volume = {:.3f} Å³'.format(al.get_volume()))

# NPT Berendsen (negative stress for compression)
dyn = NPTBerendsen(
    al,
    timestep=0.5 * units.fs,
    temperature_K=500,
    externalstress=-press_ev,
    ttime=100 * units.fs
)
dyn.run(100)

print('final   volume = {:.3f} Å³'.format(al.get_volume()))
