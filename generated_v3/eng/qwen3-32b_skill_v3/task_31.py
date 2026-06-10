from ase import bulk
from ase.calculators.emt import EMT
from ase.md import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.units import fs

atoms = bulk('Al', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
ZeroRotation(atoms)

initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume} Ang^3")

pressure_ev_per_ang3 = 10.0 / 160.21766208  # 10 GPa to eV/Ang^3

dyn = NPTBerendsen(atoms, 
                   timestep=1 * fs, 
                   temperature_K=500, 
                   pressure=pressure_ev_per_ang3)
dyn.run(100)

final_volume = atoms.get_volume()
print(f"Final volume: {final_volume} Ang^3")
