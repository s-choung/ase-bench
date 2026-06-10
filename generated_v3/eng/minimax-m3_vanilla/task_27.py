from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import MD
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Bussi

# Ag FCC 2x2x2 supercell with EMT calculator
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initial velocities at target temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# NVT MD with Bussi thermostat
dyn = MD(atoms, timestep=5 * units.fs, trajectory=None)
Bussi(dyn, temperature_K=500, taut=100 * units.fs)

def print_temperature():
    T = atoms.get_kinetic_energy() / (1.5 * len(atoms) * units.kB)
    print(f"Step {dyn.nsteps}: T = {T:.2f} K")

dyn.attach(print_temperature, interval=50)
dyn.run(200)
