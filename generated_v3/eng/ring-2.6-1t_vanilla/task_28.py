from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin

# Cu FCC 2×2×2 supercell
cu = bulk('Cu', 'fcc', a=3.61)
cu = cu.repeat([2, 2, 2])

cu.calc = EMT()

# Langevin dynamics – initial temperature not important, will be overwritten
dyn = Langevin(cu,
               dt=5.0 * units.fs,
               temperature=300.0 * units.kB,
               friction=0.02)

steps = 200
for step in range(steps):
    # linear ramp from 300 K to 600 K
    T = 300.0 + (600.0 - 300.0) * step / (steps - 1)
    dyn.temperature = T * units.kB        # update target temperature
    dyn.run(1)                             # advance one step

    if step % 50 == 0:
        print(f'step {step:4d}   T = {T:6.1f} K')
