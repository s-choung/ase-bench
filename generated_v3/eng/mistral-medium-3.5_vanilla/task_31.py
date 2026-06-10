from ase import Atoms
from ase.build import bulk
from ase.md import NPTBerendsen
from ase.calculators.emt import EMT
from ase.units import GPa, eV, Ang

al = bulk('Al', 'fcc', a=4.05, cubic=True)
al = al * (2, 2, 2)
al.calc = EMT()

P = 10 * GPa
P_eV_per_Ang3 = P * (Ang**3 / eV)

dyn = NPTBerendsen(al, timestep=1, temperature=500, pressure=P_eV_per_Ang3,
                   taut=0.1, taup=1.0, trajectory='npt.traj')
print(f"Initial volume: {al.get_volume()} Å^3")

dyn.run(100)
print(f"Final volume: {al.get_volume()} Å^3")
