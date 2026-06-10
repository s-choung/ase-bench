from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# FCC Pd 2×2×2 supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.set_calculator(EMT())

# initial velocities for 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# initial total energy
E0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# NVE dynamics, 200 steps, 2 fs timestep
dyn = VelocityVerlet(atoms, dt=2 * units.fs)
dyn.run(200)

# final total energy
E1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f'Energy difference (ΔE): {E1 - E0:.6f} eV')
