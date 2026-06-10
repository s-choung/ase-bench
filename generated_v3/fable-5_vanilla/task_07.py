from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

def total_energy(a):
    return a.get_potential_energy() + a.get_kinetic_energy()

e_init = total_energy(atoms)
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(50)
e_final = total_energy(atoms)

print(f"Initial total energy: {e_init:.6f} eV")
print(f"Final total energy:   {e_final:.6f} eV")
print(f"Energy drift:         {e_final - e_init:.6e} eV")
