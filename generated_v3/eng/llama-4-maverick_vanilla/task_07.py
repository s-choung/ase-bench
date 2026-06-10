from ase import Atoms
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT

cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[[0, 2.7, 2.7], [2.7, 0, 2.7], [2.7, 2.7, 0]], pbc=True)
cu *= (3, 3, 3)
cu.calc = EMT()
MaxwellBoltzmannDistribution(cu, 300 * ase.units.kB)
dyn = VelocityVerlet(cu, timestep=2 * ase.units.fs)
print(dyn.atoms.get_total_energy())
for _ in range(50):
    dyn.run(1)
print(dyn.atoms.get_total_energy())
