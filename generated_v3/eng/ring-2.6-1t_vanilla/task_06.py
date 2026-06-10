from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# create 2x2x2 Cu fcc supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

# initialise velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

def temperature(atoms):
    ke = atoms.get_kinetic_energy()
    n = len(atoms)
    return 2.0 * ke / (3.0 * n * units.kB)

def total_energy(atoms):
    return atoms.get_potential_energy() + atoms.get_kinetic_energy()

# initial values
T0 = temperature(atoms)
E0 = total_energy(atoms)
print(f'Initial T = {T0:.1f} K,  Energy = {E0:.4f} eV')

# Langevin dynamics
dyn = Langevin(atoms, dt=5.0, temperature=300, friction=0.01)
dyn.run(100)

# final values
T1 = temperature(atoms)
E1 = total_energy(atoms)
print(f'Final   T = {T1:.1f} K,  Energy = {E1:.4f} eV')
