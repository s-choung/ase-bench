from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build Cu FCC 2×2×2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialise velocities at 300 K and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def report(label):
    T = atoms.get_temperature()
    E_p = atoms.get_potential_energy()
    E_k = atoms.get_kinetic_energy()
    print(f"{label}: T={T:.1f} K, E_p={E_p:.3f} eV, E_k={E_k:.3f} eV, E_tot={E_p+E_k:.3f} eV")

report("Initial")

# 300 K Langevin MD, 5 fs timestep, 100 steps
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300,
               friction=0.01/units.fs)
dyn.run(100)

report("Final")
