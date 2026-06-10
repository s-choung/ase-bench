from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
from ase.io import Trajectory

# Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05).repeat((2,2,2))
atoms.calc = EMT()

# Simulation parameters
T = 500  # K
P_GPa = 10
P_eV_A3 = P_GPa * 1e9 / units._p0  # GPa to eV/Ang^3

# Print initial cell volume
V0 = atoms.get_volume()
print(f'Initial cell volume: {V0:.2f} Å^3')

# NPT Berendsen MD
dyn = NPTBerendsen(atoms, timestep=1*units.fs, temperature_K=T, pressure=P_eV_A3, taut=0.1*units.ps, taup=0.5*units.ps)
for step in range(100):
    dyn.run(1)
    
# Print final cell volume
Vf = atoms.get_volume()
print(f'Final cell volume: {Vf:.2f} Å^3')
