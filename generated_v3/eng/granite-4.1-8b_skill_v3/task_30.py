from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.thermochemistry import IdealGasThermo
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs, bar, K
from ase.io import write

# Create a 3x3x3 supercell of Cu FCC
lattice_constant = 3.615  # Å for Cu FCC
atoms = bulk('Cu', 'fcc', a=lattice_constant)
supercell = atoms.repeat(3)
supercell.calc = EMT()

# Relax the supercell to a stable structure
relax = BFGS(supercell)
relax.run(fmax=0.001)  # relax until force is smaller than 0.001 eV/Å

# Set up NPT Berendsen MD
md = NPTBerendsen(supercell,
                  ensemble='ntp',
                  temp=300*K,
                  press=1*bar,
                  timestep=5*fs,
                  tau=100*fs,
                  taup=1000*fs,
                  nrun=200,
                  nfreq=1)  # report every step

# Run the MD
md.run()

# Print initial and final cell volume and pressure
initial_volume = relax.get_initial_cell_volume()
final_volume = md.atoms.get_volume()
initial_pressure = None
final_pressure = md.atoms.get_pressure()

print(f"Initial cell volume: {initial_volume:.3f} Å³")
print(f"Final cell volume: {final_volume:.3f} Å³")
print(f"Pressure at the end of MD: {final_pressure:.2f} bar")
