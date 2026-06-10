from ase import Atoms
from ase.build import bulk
from ase.md.nvtberendsen import NVTBerendsen # Bussi is not built-in; using NVT as closest standard
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.calculators.emt import EMT
from ase import units

# Setup Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.08)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Initial conditions
temp = 500
MaxwellBoltzmannDistribution(atoms, temperature_K=temp)

# Dynamics setup
# Note: ASE built-in doesn't have Bussi/Stochastic Velocity Rescaling. 
# Using Langevin as the standard NVT built-in alternative.
dyn = Langevin(atoms, 200 * 5 * units.fs, temperature_K=temp, 
               timestep=5 * units.fs, friction=0.01)

def print_temp():
    T = atoms.get_temperature()
    print(f"Step: {dyn.get_number_of_steps()}, Temp: {T:.2f} K")

# Attach logger every 50 steps
print_temp()
dyn.attach(print_temp, interval=50)

dyn.run(200)
