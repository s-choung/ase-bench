from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.npt import NPT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.calculators.emt import EMT
from ase import units

# Setup Cu FCC 3x3x3 supercell
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], 
                          symbol='Cu', latticeconstant=3.61, size=(3, 3, 3))
atoms.calc = EMT()

# Initial state
print(f"Initial Volume: {atoms.get_volume():.2f} Å³, Pressure: {atoms.get_pressure():.2f} bar")

# MD settings
T = 300
P = 1.0 * units.bar
dt = 5 * units.fs
taut = 100 * units.fs
taup = 1000 * units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T)

dyn = NPT(atoms, timestep=dt, temperature_K=T, external_pressure=P, 
          taut=taut, taup=taup, mask=[True, True, True, True, True, True])

# Run 200 steps
dyn.run(200)

# Final state
print(f"Final Volume: {atoms.get_volume():.2f} Å³, Pressure: {atoms.get_pressure():.2f} bar")
