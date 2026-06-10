from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Initial conditions
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Convert pressure from GPa to eV/Ang^3
pressure_GPa = 10
pressure_eV_A3 = pressure_GPa * units.GPa

# Print initial cell volume
initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume:.2f} Ang^3")

# Run NPT MD
dyn = NPTBerendsen(atoms, timestep=2*units.fs, temperature_K=500, pressure_au=pressure_eV_A3, taut=100*units.fs, taup=100*units.fs)
dyn.run(100)

# Print final cell volume
final_volume = atoms.get_volume()
print(f"Final volume: {final_volume:.2f} Ang^3")
