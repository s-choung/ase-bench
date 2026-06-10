from ase import Atoms
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase import units

a = 3.6
atoms = bulk('Al', 'fcc', a=a)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

pressure = 10 * units.GPa
temperature = 500 * units.K
timestep = 5 * units.fs

npt = NPTBerendsen(atoms, timestep, temperature, pressure,
                   trajectory='npt.traj')

initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume:.6f} Ang^3")

npt.run(100)

final_volume = atoms.get_volume()
print(f"Final volume: {final_volume:.6f} Ang^3")
