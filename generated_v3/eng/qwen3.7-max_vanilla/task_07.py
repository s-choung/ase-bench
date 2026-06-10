from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

e_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

e_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial Total Energy: {e_init:.6f} eV")
print(f"Final Total Energy:   {e_final:.6f} eV")
print(f"Energy Drift:         {e_final - e_init:.6e} eV")
