from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
import numpy as np

a = 3.6  # Cu lattice constant
bulk = Atoms('Cu4', cell=[(0, a, a), (a, 0, a), (a, a, 0)], pbc=True)
bulk.calc = EMT()

np.random.seed(0)
MaxwellBoltzmannDistribution(bulk, temperature_K=300)
Stationary(bulk)

dyn = VelocityVerlet(bulk, timestep=1 * units.fs)
def printenergy(a=bulk):
    ekin = a.get_kinetic_energy()
    epot = a.get_potential_energy()
    print(f'Energy: {ekin + epot:.3f} eV (kin={ekin:.3f}, pot={epot:.3f})')

printenergy()
dyn.run(50)
printenergy()
