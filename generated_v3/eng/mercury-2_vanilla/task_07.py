from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocityverlet import VelocityVerlet
from ase import units

# Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.set_calculator(EMT())

# Initial temperature 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# MD parameters
dt = 1 * units.fs
dyn = VelocityVerlet(atoms, dt)

# Record initial energies
Epot_i = atoms.get_total_energy()
Ekin_i = atoms.get_kinetic_energy()
print(f'Initial total energy: {Epot_i + Ekin_i:.6f} eV')

# Run 50 steps
dyn.run(50)

# Record final energies
Epot_f = atoms.get_total_energy()
Ekin_f = atoms.get_kinetic_energy()
print(f'Final total energy:   {Epot_f + Ekin_f:.6f} eV')
