from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.io.trajectory import Trajectory

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = Bussi(atoms, timestep=5 * units.fs, temperature_K=500,
           taut=0.5 / units.fs, trajectory='ag_md.traj')

def print_temp():
    print(f"Step {md.nsteps:4d}: T = {atoms.get_temperature():.2f} K")

md.attach(print_temp, interval=50)
md.run(200)
