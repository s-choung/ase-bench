from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

E_init = atoms.get_total_energy()
print(f"Initial total energy: {E_init:.4f} eV")

dyn = VelocityVerlet(atoms, 1.0 * units.fs)
dyn.run(50)

E_final = atoms.get_total_energy()
print(f"Final total energy:   {E_final:.4f} eV")
