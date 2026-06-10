import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

class RampedLangevin(Langevin):
    def set_temperature(self, T):
        self.temperature_K = T
        if isinstance(self.friction, float) or np.isscalar(self.friction):
            self.sigma = np.sqrt(2 * self.friction * units.kB * T * self.atoms.get_masses() / self.dt)
        else:
            self.sigma = np.sqrt(2 * self.friction * units.kB * T / self.dt) * np.sqrt(self.atoms.get_masses())[:, np.newaxis]

atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300 * units.kB, force_temperature=True)
dyn = RampedLangevin(atoms, timestep=5.0, temperature_K=300, friction=0.002)

for step in range(200):
    T_target = 300 + 300 * (step + 1) / 200.0
    dyn.set_temperature(T_target)
    dyn.run(1)
    if step % 50 == 0:
        print(f'Step {step}: T = {atoms.get_temperature():.2f} K')
