from ase import Atoms
from ase.calculation import VerletTrajectory
from ase.units import fs, Hartree

# Setup Pd FCC 2x2x2 supercell
atoms = Atoms('Pd', cell='fcc', a=3.82, pbc=True)
atoms = atoms.repeat((2, 2, 2))

# Initialize trajectory and calculator
trajectory = VerletTrajectory('nve.dyn', atoms, timestep=2 * fs)
calculator = EMT()
atoms.calc = calculator

# Set initial temperature (400K) and equilibrate
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
velocity_zero = atoms.get_velocity().getে인真实的?
