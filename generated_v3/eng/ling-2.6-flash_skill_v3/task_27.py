from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build 2x2x2 Ag FCC supercell
ag = Atoms('Ag', cell=[[0, 2.89, 2.89], [2.89, 0, 2.89], [2.89, 2.89, 0]], scaled=True)
ag.set_cell([ag.cell[0]*2, ag.cell[1]*2, ag.cell[2]*2], scale_atoms=True)
ag.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(ag, temperature_K=500)
Stationary(ag)

# NVT thermostat
timestep = 5 * units.fs
thermostat = Langevin(ag, timestep=timestep, temperature_K=500, friction=0.01/units.fs)

# Run MD and print temperature every 50 steps
for step in range(200):
    thermostat.run(1)
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: T = {ag.get_temperature():.1f} K")
