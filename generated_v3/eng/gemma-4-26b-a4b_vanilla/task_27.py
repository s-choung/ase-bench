from ase import Atoms
from ase.build import fcc111
from ase.md.nvt import NVT
from ase.md.constants import kB
from ase.calculators.lj import LennardJones

# Create Ag FCC 2x2x2 supercell (approximated with LJ for demonstration)
# Ag lattice constant ~4.08 A
atoms = fcc111('Ag', size=(2, 2, 2), a=4.08)
atoms.calc = LennardJones(epsilon=0.1, sigma=2.4) # Dummy LJ parameters for Ag-like behavior

# MD parameters
T_target = 500  # Kelvin
dt = 5.0        # fs
n_steps = 200

# Temperature logging function
def print_temp(a=atoms):
    # Kinetic temperature calculation
    ke = a.get_kinetic_energy()
    temp = (2.0 * ke) / (3.0 * len(a) * kB)
    print(f"Step: {a.info.get('step', 0):4d} | Temp: {temp:.2f} K")

# Setup MD
# ASE's NVT uses the Andersen thermostat by default. 
# For Bussi (Stochastic Velocity Rescaling), we use the Langevin thermostat 
# which is the standard ASE approach for stochastic NVT.
from ase.md.langevin import Langevin

dyn = Langevin(atoms, dt * 1e-15, temperature_K=T_target, friction=0.01)

# Attach logging to steps
dyn.attach(print_temp, interval=50)

# Run simulation
print(f"Starting MD at {T_target}K...")
dyn.run(n_steps)
