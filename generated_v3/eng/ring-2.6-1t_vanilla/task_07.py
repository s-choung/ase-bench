from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet

# create FCC Cu (≈3.615 Å lattice constant)
atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()

# initial Maxwell–Boltzmann velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# initial total energy = kinetic + potential
E_initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print('Initial total energy:', E_initial, 'eV')

# NVE integration with VelocityVerlet (1 fs time step)
dyn = VelocityVerlet(atoms, dt=1.0 * units.fs)
dyn.run(50)                     # 50 MD steps

# final total energy
E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print('Final total energy:', E_final, 'eV')
