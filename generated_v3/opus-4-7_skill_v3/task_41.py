from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=1.0*units.fs, trajectory='cu_md.traj')
dyn.run(10)

frames = read('cu_md.traj', index=':')
print(f"Total frames: {len(frames)}")
print(f"Last frame energy: {frames[-1].get_potential_energy():.6f} eV")
