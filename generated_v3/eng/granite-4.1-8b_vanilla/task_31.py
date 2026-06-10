from ase import Atoms
from ase.build import fcc111
from ase.md import NPTBerendsen
from ase.calculators.emt import EMT
from ase.units import GPa, eV, Angstrom

# Create Al FCC 2x2x2 supercell
al = fcc111('Al', size=(2, 2, 2), vacuum=10)
calculator = EMT()
al.set_calculator(calculator)

# Set temperature and pressure
temperature = 500  # K
pressure = 10 * GPa  # Convert GPa to eV/Ang^3 using ASE units conversion
# ASE provides a conversion factor: 1 GPa ≈ 0.160217656 eV/Ang^3
pressure_eV = pressure * 0.160217656  # Convert pressure to eV/Ang^3

# Apply NPTBerendsen ensemble
md = NPTBerendsen(atoms=al,
                  temperature=temperature,
                  pressure=pressure_eV,
                  timestep=4.0,  # femtoseconds
                  constraints=[],
                  logfile='md.log',
                  dilatation=True,
                  nstlog=10,
                  nscm=100,
                  nstenergy=10,
                  nsttemp=10,
                  nstcalcenergy=10,
                  gamma_l=1.0,
                  islow=100,
                  nstlim=100)

# Print initial cell volume
initial_volume = al.get_volume()
print(f"Initial cell volume: {initial_volume:.3f} Å^3")

# Run the MD simulation
md.run()

# Print final cell volume
final_volume = al.get_volume()
print(f"Final cell volume: {final_volume:.3f} Å^3")
