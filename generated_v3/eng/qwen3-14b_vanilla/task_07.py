from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.set_calculator(EMT())
atoms.set_initial_velocities(temperature=300)
dyn = VelocityVerlet(atoms, dt=1.0)
print('Initial energy:', atoms.get_total_energy())
for _ in range(50):
    dyn.step()
print('Final energy:', atoms.get_total_energy())
