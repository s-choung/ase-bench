import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Cu fcc 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
atoms.calc = EMT()

# Langevin MD parameters
timestep = 5.0 * units.fs
dyn = Langevin(atoms, timestep, temperature=300 * units.kB, friction=0.01)

# Temperature ramp 300 K → 600 K over 200 steps (5 fs each)
for step in range(200):
    T = 300 + 300 * (step + 1) / 200
    dyn.temperature = T * units.kB
    dyn.step()
    if (step + 1) % 50 == 0:
        print(f"Step {step+1}, Temperature = {T:.1f} K")
