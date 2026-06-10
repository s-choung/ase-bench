"""T5 Vanilla: Langevin MD of Cu at 300K"""
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Langevin

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

dyn = Langevin(atoms, timestep=5.0, temperature=300, friction=0.01)
dyn.run(20)
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
print(f"Temperature: {atoms.get_temperature():.1f} K")
