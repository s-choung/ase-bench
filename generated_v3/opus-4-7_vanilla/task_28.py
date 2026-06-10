import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

T_start, T_end, n_steps = 300, 600, 200
MaxwellBoltzmannDistribution(atoms, temperature_K=T_start)

dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=T_start, friction=0.01)

temps = np.linspace(T_start, T_end, n_steps)

for i, T in enumerate(temps):
    dyn.set_temperature(temperature_K=T)
    dyn.run(1)
    if (i + 1) % 50 == 0:
        ekin = atoms.get_kinetic_energy() / len(atoms)
        T_inst = ekin / (1.5 * units.kB)
        print(f"Step {i+1}: target T = {T:.1f} K, instantaneous T = {T_inst:.1f} K")
