from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Initial velocity
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Langevin MD with temperature ramp
temp_start = 300
temp_end = 600
n_steps = 200
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=temp_start, friction=0.01/units.fs)

def temp_ramp(dyn, temp_start, temp_end, n_steps):
    for i in range(n_steps):
        temp_current = temp_start + (temp_end - temp_start) * i / (n_steps - 1)
        dyn.set_temperature(temp_current)
        dyn.run(1)
        if i % 50 == 0:
            print(f'Step {i+1}, Temperature: {atoms.get_temperature():.2f} K')

temp_ramp(dyn, temp_start, temp_end, n_steps)
