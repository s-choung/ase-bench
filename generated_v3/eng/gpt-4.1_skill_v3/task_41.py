from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase.io import read

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

trajfile = 'md.traj'
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs, trajectory=trajfile)
dyn.run(10)

frames = list(read(trajfile, index=':'))
print(f"Total frames: {len(frames)}")
frames[-1].calc = EMT()
print(f"Energy of last frame: {frames[-1].get_potential_energy():.6f} eV")
