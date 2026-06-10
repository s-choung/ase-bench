import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermo import NVTBerendsen
from ase.md.verlet import VelocityVerlet
from ase.units import eV, fs
from ase.io import write

# Create an Ag FCC supercell 2x2x2
atom=Atoms('Ag*8', positions=[[0,0,0],
                              [0.5,0.5,0.5],
                              [0,0.5,0.5],
                              [0.5,0,0.5],
                              [0.5,0.5,0.],
                              [0,0,0.5],
                              [0.5,0.,0.],
                              [0.,0.5,0.]])

# Set lattice vectors (FCC with 2x2x2 conventional cell)
fcc_vec = np.array([[-0.5,0.5,0.5],[0.5,-0.5,0.5],[0.5,0.5,-0.5]])
atom.set_cell(fcc_vec)
atom.set_pbc(True)

# Calculator
atom.set_calculator(EMT())
print('Initial energy:', atom.get_potential_energy())

# Initial velocities from Maxwell distribution at 1000 K
temperature0 = 1000.0
np.random.seed(42)
kinetic0 = 0.5 * (len(atom) * 1.507 * temperature0)  # Dulong‑Petit for Ag
for i in range(len(atom)):
    v = np.random.randn(3) * np.sqrt(kinetic0 / (len(atom) * 1.507))
    atom.set_initial_magnetic_moments([0])          # Si mag
    atom.set_velocities(v)

# NVT with Bussi thermostat (velocity Verlet)
dyn = VelocityVerlet(atom, dt=5*fs)
thermo = NVTBerendsen(friction=0.05, temperature0=temperature0, timestep=20*fs)

for step in range(200):
    dyn.step(vturb=None, logfile=None, timestep=dt, log_every_n=None)
    # Apply thermostat after the integration step
    atom kinetic energy change
    mass = atom.get_masses().mean()
    kinetic = 0.5 * sum(atom.get_momenta()**2 / mass)
    temperature = kinetic * (mass * fs**2 / ev)
    print(f'Step {step:4d}, T = {temperature/1000:.2f} K')
