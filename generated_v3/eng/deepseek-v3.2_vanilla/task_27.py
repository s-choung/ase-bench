import ase
from ase import Atoms
from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase import units
from ase.io.trajectory import Trajectory

# Create FCC Ag supercell
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True) * (2, 2, 2)
atoms.calc = ase.calculators.emt.EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Create MD simulation
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=500, friction=0.002)

# Temperature logging function
steps_log = 50
def print_temp(atoms=atoms):
    E_kin = atoms.get_kinetic_energy()
    temp = E_kin / (1.5 * len(atoms) * units.kB)
    print(f'Step {dyn.get_number_of_steps()}: T = {temp:.2f} K')

# Attach temperature logging
dyn.attach(print_temp, interval=steps_log)

# Run MD
dyn.run(200)
