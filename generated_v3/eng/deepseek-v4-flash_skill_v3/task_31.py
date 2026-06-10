from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.nptberendsen import NPTBerendsen
from ase.io.trajectory import Trajectory

# Convert pressure: 1 GPa ≈ 0.0062415 eV/Å³
pressure_GPa = 10.0
pressure_eV_per_Ang3 = pressure_GPa * units.GPa  # units module: 1 GPa = 0.0062415 eV/Å³

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Initial volume
print(f"Initial volume: {atoms.get_volume():.4f} Å³")

# Set up MD
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# NPTBerendsen parameters
timestep = 1.0 * units.fs
taut = 100 * units.fs      # temperature relaxation time
taup = 1000 * units.fs     # pressure relaxation time
compressibility = 4e-4 / units.GPa  # in 1/GPa, convert to 1/(eV/Å³)

md = NPTBerendsen(atoms,
                  timestep=timestep,
                  temperature_K=500,
                  pressure_au=pressure_eV_per_Ang3,
                  taut=taut,
                  taup=taup,
                  compressibility_au=compressibility,
                  trajectory='npt.traj')

# Run 100 steps
md.run(steps=100)

# Final volume
print(f"Final volume: {atoms.get_volume():.4f} Å³")
