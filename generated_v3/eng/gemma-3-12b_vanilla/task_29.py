from ase.build import fcc
from ase.md.velocityverlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.units import kJ, fs

atoms = fcc('Pd', size=(2, 2, 2))
atoms.get_all_neighbors()

calculator = EMT()
atoms.calc = calculator

N = len(atoms)
temp = 500 * kJ / (1.380649e-23 * 1000)
atoms.get_potential_energy()
atoms.set_momenta(temp)

dt = 2 * fs

md = VelocityVerlet(atoms, dt)

initial_energy = atoms.get_potential_energy() + 0.5 * atoms.get_kinetic_energy()

for i in range(200):
    md.run(1)

final_energy = atoms.get_potential_energy() + 0.5 * atoms.get_kinetic_energy()

energy_difference = final_energy - initial_energy

print(energy_difference)
