from ase import Atoms
from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase.md.nptberendsen import NVTBerendsen
from ase.calculators.emt import EMT
from ase.units import fs, kcal

# Create a 2x2x2 supercell of FCC Ag
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))

# Use EMT calculator
atoms.calc = EMT()

# Initialize velocities for MD (298 K)
MaxwellBoltzmannDistribution(atoms, 298 * kcal)

# Initialize NVT MD with the Berendsen thermostat
dyn = NVTBerendsen(atoms, t_target=500 * kcal, tau=100 * fs, dt=5 * fs)

# Set a custom thermostat: Bussi thermostat
class BussiThermostat:
    def __init__(self, atoms, temperature, time_constant, time_step):
        self.atoms = atoms
        self.temperature = temperature
        self.time_constant = time_constant
        self.time_step = time_step
        self.beta = 1 / (self.temperature * 0.695039)
        self.alpha = time_step / (2 * time_constant)
        self.random_force = 1
        self.pre_velocity = atoms.get_velocities().copy()

    def step(self):
        self.atoms.set_velocities((1 - self.alpha) * self.atoms.get_velocities())
        random_force = (numpy.random.random(self.atoms.get_positions().shape) - 0.5) / 3 ** 0.5
        self.atoms.set_velocities(self.atoms.get_velocities() + self.random_force * random_force * self.alpha * (2 * self.temperature / self.atoms.get_masses()))
        self.pre_velocity = self.atoms.get_velocities().copy()
        
    def run_step(self):
        self.step()
        kinetic_energy = 0.5 * numpy.sum(self.atoms.get_masses() * self.atoms.get_velocities() ** 2)
        current_temperature = 2 * kinetic_energy / (len(self.atoms) * 1.5)  # kB=1 in ASE
        return 1 / self.beta * numpy.log(numpy.sum(self.pre_velocity ** 2) / numpy.sum(self.atoms.get_velocities() ** 2))

bussi_thermostat = BussiThermostat(atoms, 500 * kcal, 100 * fs, 5 * fs)

# Suppress Langevin damping for T communication
dyn.attach(bussi_thermostat.run_step, interval=1)

# Record temperatures every 50 steps
temperatures = []

def record_temperature(step):
    if step % 50 == 0:
        temperature = bussi_thermostat.run_step()
        temperatures.append(temperature)

for step in range(200):
    dyn.run(1)
    bussi_thermostat.run_step()
    record_temperature(step)

# Convert temperature back to Kelvin for printing
print("Recorded Temperatures (K):", [temp / kcal for temp in temperatures])
