from ase import Atoms, units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet

# FCC Cu bulk
atoms = Atoms('Cu', cell=[4, 4, 4], pbc=True)
atoms *= (2, 2, 2)

# EMT calculator
atoms.calc = EMT()

# Initial velocities (300 K)
MaxwellBoltzmannDistribution(atoms, 300*units.kB)

# NVE dynamics
dyn = VelocityVerlet(atoms, dt=5*units.fs)

# Energies
e_init = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# Run 50 steps
dyn.run(50)

# Final energy
e_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()

print("Initial E:", e_init, "Final E:", e_final)
