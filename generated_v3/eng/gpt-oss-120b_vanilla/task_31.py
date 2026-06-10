from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
import numpy as np

# conversion GPa → eV/Å³
def gpa_to_ev_per_ang3(GPa):
    # 1 Pa = 6.241509074460763e-12 eV/Å³
    return GPa * 1e9 * 6.241509074460763e-12

# create Al FCC 2×2×2 supercell
al = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)

# attach calculator
al.calc = EMT()

# initial velocities (500 K)
MaxwellBoltzmannDistribution(al, temperature_K=500)

# NPT parameters
dt = 2.0               # fs
temperature = 500.0   # K
pressure = gpa_to_ev_per_ang3(10.0)  # eV/Å³

dyn = NPTBerendsen(al, dt * 1e-15, temperature_K=temperature,
                    pressure=pressure, tscale=0.1, pscale=0.1)

# record initial volume
vol_initial = al.get_volume()
print(f'Initial volume: {vol_initial:.3f} Å³')

# run dynamics
dyn.run(100)

# record final volume
vol_final = al.get_volume()
print(f'Final volume: {vol_final:.3f} Å³')
