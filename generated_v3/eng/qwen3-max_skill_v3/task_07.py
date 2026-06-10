from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def get_total_energy(atoms):
    return atoms.get_potential_energy() + atoms.get_kinetic_energy()

E_initial = get_total_energy(atoms)
print(f"Initial total energy: {E_initial:.6f} eV")

md = VelocityVerlet(atoms, timestep=5*units.fs)
md.run(50)

E_final = get_total_energy(atoms)
print(f"Final total energy: {E_final:.6f} eV")
