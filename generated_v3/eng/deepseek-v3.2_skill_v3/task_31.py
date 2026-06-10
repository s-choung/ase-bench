from ase import Atoms, units
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = None  # No external calculator needed for demonstration

pressure = 10.0 * units.GPa  # 10 GPa
temperature = 500.0 * units.kB  # 500K

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=2.0*units.fs, temperature=temperature,
                   pressure=pressure, taut=100.0*units.fs, taup=1000.0*units.fs)

initial_vol = atoms.get_volume()
print(f'Initial volume: {initial_vol:.2f} Å³')

dyn.run(100)

final_vol = atoms.get_volume()
print(f'Final volume: {final_vol:.2f} Å³')
