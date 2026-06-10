from ase import Atoms
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT
from ase.io import write

# Create Al FCC 2x2x2 supercell
al = Atoms('Al', positions=[[0, 0, 0]], cell=[[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]], pbc=True)
al = al.repeat((2, 2, 2))

# Set calculator
al.calc = EMT()

# Set MD parameters
T = 500  # K
P = 10 * 160.21766208e-21  # GPa to eV/Ang^3
nsteps = 100
ttime = 25  # fs
ptime = 75  # fs

# Print initial volume
print("Initial volume:", al.get_volume())

# Run NPT MD
dyn = NPTBerendsen(al, 1 * ase.units.fs, T, P, ttime, ptime)
dyn.run(nsteps)

# Print final volume
print("Final volume:", al.get_volume())
