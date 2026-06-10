from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT
from ase.units import fs, kB

# Create Cu FCC 3x3x3 supercell
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                          symbol='Cu',
                          size=(3, 3, 3),
                          pbc=True)

# Attach EMT potential
atoms.calc = EMT()

# Initialize velocities at 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# NPT Berendsen parameters
timestep = 5 * fs
taut = 100 * fs
taup = 1000 * fs
temperature_K = 300
pressure_bar = 1

# Create NPT dynamics
dyn = NPTBerendsen(atoms, timestep, temperature_K, taut, pressure_bar * 1e5 / kB, taup)

# Print initial volume and pressure
print(f"Initial volume: {atoms.get_volume()}")
print(f"Initial pressure: {atoms.get_kinetic_pressure() / (1e5 / kB):.2f} bar")

# Run MD
for _ in range(200):
    dyn.run(1)

# Print final volume and pressure
print(f"Final volume: {atoms.get_volume()}")
print(f"Final pressure: {atoms.get_kinetic_pressure() / (1e5 / kB):.2f} bar")
