from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.units import fs, eV

cell = 2 * 2.75 * (2**0.5)
atoms = Atoms('Pd', cell=[[cell, 0, 0], [0, cell, 0], [0, 0, cell]])
atoms.set_calculator(EMT())
MaxwellBoltzmannDistribution(atoms, 500.0)

print(f"Initial energy: {atoms.get_potential_energy() + atoms.get_kinetic_energy():.4f} eV")
initial_total_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

dyn = VelocityVerlet(atoms, 2.0 * fs)

def print_energy(a):
    print(f"Step {a.nsteps}: E={a.get_potential_energy() + a.get_kinetic_energy():.4f} eV")

dyn.attach(print_energy, interval=20, n=20)
dyn.run(200)

final_total_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Energy difference: {final_total_energy - initial_total_energy:.4f} eV")
