from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Al FCC 2×2×2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

v0 = atoms.get_volume()                     # initial volume

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# 10 GPa → eV/Å³ (1 Pa = 6.24150907446076e‑12 eV/Å³)
pressure = 10e9 * 6.24150907446076e-12

dyn = NPTBerendsen(atoms,
                   timestep=1*units.fs,
                   temperature_K=500,
                   pressure=pressure,
                   ttime=100*units.fs,
                   pfactor=100*units.fs)
dyn.run(100)

v1 = atoms.get_volume()                     # final volume
print(f'Initial volume: {v0:.3f} Å³')
print(f'Final volume:   {v1:.3f} Å³')
