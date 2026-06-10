from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

# Build Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * [2, 2, 2]
atoms.set_calculator(EMT())

# Convert pressure: 10 GPa -> eV/Ang^3
# 1 eV/Ang^3 = 160.2176634 GPa
pressure_GPa = 10.0
pressure_eV_per_A3 = pressure_GPa * 1e9 / (units.kB * 300)  # placeholder, will replace
# Correct conversion:
pressure_eV_per_A3 = pressure_GPa * 1e9 / 1.602176634e11  # 1 eV/Ang^3 = 1.602e11 Pa

print('Initial volume:', atoms.get_volume())

# NPT Berendsen dynamics
dyn = NPTBerendsen(atoms,
                   temperature_K=500,
                   pressure_eV_per_A3=pressure_eV_per_A3,
                   timestep=1*units.fs,
                   taut=100*units.fs,
                   taup=1000*units.fs)
dyn.run(100)

print('Final volume:', atoms.get_volume())
