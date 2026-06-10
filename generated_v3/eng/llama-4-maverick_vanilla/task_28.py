from ase import Atoms
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic

atoms = FaceCenteredCubic('Cu', size=(2, 2, 2))
atoms.calc = EMT()

dyn = Langevin(atoms, timestep=5 * 1e-15, temperature_K=300, friction=1e12)
for i in range(200):
    dyn.run(1)
    if i % 50 == 0:
        print(f'Step {i+1}, Temperature: {atoms.get_temperature():.2f} K')
    dyn.temperature_K = 300 + (i+1) / 200 * (600 - 300)
