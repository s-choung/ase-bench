from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.ensemble import NPTBerendsen
from ase.units import GPa, eV, Angstrom

# Create Al FCC 2x2x2 supercell
atoms = Atoms('Al256', cell=[[4,4,0],[0,4,4],[4,0,4]]*2, pbc=True)
atoms.set_calculator(EMT())

# Convert pressure: 10 GPa to eV/Ang^3
pressure_eV = 10 * GPa / (eV / Angstrom**3)

# Initialize velocities and print initial volume
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
print(f"Initial volume: {atoms.get_volume():.2f} Angstrom^3")

# Run NPT MD
dyn = NPTBerendsen(atoms, timestep=1.0*0.5, temperature=500, pressure=pressure_eV)
dyn.run(100)

# Print final volume
print(f"Final volume: {atoms.get_volume():.2f} Angstrom^3")
