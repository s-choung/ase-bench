from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet

a = 3.9  # lattice constant for Pd
atoms = Atoms('Pd', positions=[(0, 0, 0)], cell=a*[(1, 0, 0), (0, 1, 0), (0, 0, 1)], pbc=True)
atoms *= (2, 2, 2)
atoms.set_calculator(EMT())

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
dyn = VelocityVerlet(atoms, timestep=2*1e-15, trajectory=None)
E_init = atoms.get_total_energy()
dyn.run(200)

print(f"Energy change: {atoms.get_total_energy() - E_init:.6f} eV")
