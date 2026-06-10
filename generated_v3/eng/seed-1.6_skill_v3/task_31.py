from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05).repeat((2,2,2))
atoms.calc = EMT()

# Initial volume
initial_vol = atoms.get_volume()

# Convert 10 GPa to eV/Å³ (1 GPa ≈ 6.2415e-3 eV/Å³)
pressure = 10 * 6.241509074e-3

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Set up NPT Berendsen MD
md = NPTBerendsen(
    atoms,
    timestep=2*units.fs,
    temperature_K=500,
    pressure=pressure,
    tau_t=200*units.fs,
    tau_p=2000*units.fs
)

# Run 100 steps
md.run(100)

# Final volume
final_vol = atoms.get_volume()

# Print results
print(f'Initial volume: {initial_vol:.2f} Å³')
print(f'Final volume: {final_vol:.2f} Å³')
