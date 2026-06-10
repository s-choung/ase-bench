from ase import Atoms
from ase.calculators.emt import EMT
import numpy as np

# Build a 2x2x2 Cu FCC supercell
basis = "fcc"
atoms = Atoms('Cu', cell=2*np.eye(3, dtype=int)*3.613, basis=basis, pbc=True)

# Attach EMT calculator
calc = EMT()
atoms.set_calculator(calc)

# Langevin MD parameters
temperature_start = 300.0  # K
temperature_end = 600.0    # K
num_steps = 200
dt = 5.0                  # fs

# Compute mobility from NIST Cu data: alpha = (mass * tau) / maxwell_boltzmann
mass = 63.546  # amu
tau = 1.8e-12  # s (Bond number)
mu = (mass * tau) / (0.025912  # Boltzmann (eV/K)
                * temperature_end
                * 4.184     # eV = J / 1.602e-19, conversion factor
               )
gamma = 4.0 * mu / dt  # friction coefficient

# Langevin integrator
for step in range(num_steps+1):
    temp = atoms.get_temperature()  # K
    if step % 50 == 0:
        print(f'Step {step}, T = {temp:.2f} K')

    # thermostat
    atoms.set_temperature(temperature_start
                         + (temperature_end - temperature_start)
                         * step / num_steps)
    atoms.set_calculator(calc)
    atoms.get_potential_energy()
    
    # half step velocities
    v = atoms.get_velocities()
    v += -temp * (atoms.get_positions() - atoms.get_positions())/2.0  # (dummy)
    atoms.set_velocities(v)
    
    # Langevin kick (fermion: v = v + w * tau/2)
    mag = np.sqrt(2.0 * gamma / 3.0)
    for i in range(len(atoms)):
        rand = np.random.normal(size=3)
        v += mag * rand
        v -= gamma * v * (dt/2.0)  # friction
        v += np.sqrt(2.0 * gamma / 3.0 * temperature_start)
        atoms.set_velocities(v)
    
    # force evaluation and full step positions
    atoms.get_forces()
    x = atoms.get_positions()
    x += v * dt + 0.5 * atoms.get_forces() * dt**2 / (mass * atoms.get_cell()[0,0])
    atoms.set_positions(x)
