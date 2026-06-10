from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.units import fs
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

def total_energy(atoms):
    return atoms.get_kinetic_energy() + atoms.get_potential_energy()

e_init = total_energy(atoms)
print(f"Initial total energy: {e_init:.6f} eV")

dyn = VelocityVerlet(atoms, timestep=1.0 * fs)
dyn.run(50)

e_final = total_energy(atoms)
print(f"Final   total energy: {e_final:.6f} eV")
print(f"Energy drift:         {e_final - e_init:.6f} eV")
