from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs, GPa, eV, Ang, Pa

# Al FCC 2x2x2 supercell
al = Atoms('Al', cell=4.05*[[1,0,0],[0,1,0],[0,0,1]],
           positions=[[0,0,0],[0.5,0.5,0],[0.5,0,0.5],[0,0.5,0.5]], pbc=True)
supercell = al * (2,2,2)
supercell.calc = EMT()

# Initial setup
MaxwellBoltzmannDistribution(supercell, 500)
initial_vol = supercell.get_volume()

# Pressure conversion (10 GPa to eV/Ang³)
target_press = 10 * GPa / (eV / Ang**3)
# Al's isothermal compressibility (1.3e-12 Pa⁻¹ to Ang³/eV)
compress_au = 1.3e-12 * Pa / (eV / Ang**3)

# NPT Berendsen MD
md = NPTBerendsen(supercell, timestep=1*fs, temperature_K=500,
                  pressure_au=target_press, taut=0.5e3*fs, taup=1e3*fs,
                  compressibility_au=compress_au)
md.run(100)

# Output volumes
print(f'Initial volume: {initial_vol:.2f} Ang³')
print(f'Final volume: {supercell.get_volume():.2f} Ang³')
