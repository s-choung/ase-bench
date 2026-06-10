from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# 3×3×3 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

# initial state
V0 = atoms.get_volume()
P0 = atoms.get_pressure()

# velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# NPT MD
dyn = NPTBerendsen(atoms,
                   timestep=5 * units.fs,
                   temperature_K=300,
                   pressure=1 * units.bar,
                   tau_t=100 * units.fs,
                   tau_p=1000 * units.fs)
dyn.run(200)

# final state
Vf = atoms.get_volume()
Pf = atoms.get_pressure()

print(f'Initial volume: {V0:.3f} Å³, pressure: {P0:.3f} kBar')
print(f'Final volume: {Vf:.3f} Å³, pressure: {Pf:.3f} kBar')
