from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.npt import NPTBerendsen

# FCC Al 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.set_calculator(EMT())

# pressure conversion: 1 GPa = 6.241509074e-3 eV/Å³
GPa_to_eV_A3 = 6.241509074e-3
target_pressure = 10 * GPa_to_eV_A3  # 10 GPa

# NPT Berendsen MD
dt = 1 * units.fs
dyn = NPTBerendsen(atoms, dt,
                    temperature_K=500,
                    pressure=target_pressure,
                    ttime=100 * units.fs,
                    pfactor=1000 * units.fs)

print('Initial volume:', atoms.get_volume())
for _ in range(100):
    dyn.run(1)
print('Final volume:', atoms.get_volume())
