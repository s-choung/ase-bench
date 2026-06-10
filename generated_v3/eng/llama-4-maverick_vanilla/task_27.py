from ase import Atoms
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.md.nvtberendsen import NVTBerendsen  # Not used, using Bussi instead
from ase.md.nvt import NVT  # Using Bussi thermostat through this interface
from ase.calculators.emt import EMT

a = 4.09  # Ag lattice constant
ag = Atoms('Ag', positions=[[0, 0, 0]], cell=[[a/2, a/2, 0], [a/2, 0, a/2], [0, a/2, a/2]], pbc=True)
ag *= (2, 2, 2)
ag.calc = EMT()
MaxwellBoltzmannDistribution(ag, temperature_K=500)
dyn = NVT(ag, timestep=5*1e-15, temperature_K=500, taut=0.5e-12, fixcm=True)
dyn.attach(lambda atoms: print(atoms.get_temperature()), interval=50)
dyn.run(200)
