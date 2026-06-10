from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.io import read, Trajectory
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

with Trajectory('md.traj', 'w') as traj:
    def write_step():
        traj.write(atoms)
    VelocityVerlet(atoms, 1 * units.fs).run(10, on_step=write_step)

atoms_list = read('md.traj', index=':')
atoms_list[-1].calc = EMT()
print(f"Total frames: {len(atoms_list)}")
print(f"Last frame energy: {atoms_list[-1].get_potential_energy()} eV")
