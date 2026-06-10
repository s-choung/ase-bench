from ase.build import fcc
from ase.md.velocityverlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.units import kJ

atoms = fcc('Cu', size=2.5)
calc = EMT()
atoms.calc = calc

n_steps = 50
temperature = 300.0 * kJ / atoms.get_potential_energy()
md = VelocityVerlet(atoms, dt=0.005)
md.initialize(temperature)

initial_energy = atoms.get_potential_energy() + sum([0.5 * a.momentum.dot(a.momentum) / atoms.get_potential_energy() for a in atoms])
print(f"Initial energy: {initial_energy}")

md.run(n_steps)

final_energy = atoms.get_potential_energy() + sum([0.5 * a.momentum.dot(a.momentum) / atoms.get_potential_energy() for a in atoms])
print(f"Final energy: {final_energy}")
