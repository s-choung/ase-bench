from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.units import fs

# Build Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms *= (2, 2, 2)

# Setup
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Langevin MD
ensemble = Langevin(atoms, timestep=5*fs, temperature_K=300, friction=0.01/fs)

def run_ramp():
    for step in range(200):
        current_temp = atoms.get_temperature()
        if step % 50 == 0:
            print(f"Step {step}: T = {current_temp:.1f} K")
        # Ramp temperature from 300K to 600K linearly
        T_target = 300 + (600 - 300) * step / 199
        ensemble.temperature_K = T_target
        ensemble.run(1)  # run one step

    # Final print
    print(f"Step 199: T = {atoms.get_temperature():.1f} K")

run_ramp()
