from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Convert 10 GPa to eV/Ang^3
pressure_eV_Ang3 = 10 * units.GPa

# Print initial volume
initial_volume = atoms.get_volume()
print(f"Initial cell volume: {initial_volume:.2f} Ang^3")

# Run NPT MD
npt = NPTBerendsen(atoms, timestep=2*units.fs, temperature_K=500, 
                   pressure_au=pressure_eV_Ang3, tau_t=100*units.fs, tau_p=500*units.fs)
npt.run(100)

# Print final volume
final_volume = atoms.get_volume()
print(f"Final cell volume: {final_volume:.2f} Ang^3")
