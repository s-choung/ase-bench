from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
atoms.set_calculator(EMT())

# MD settings
dt = 5 * units.fs          # 5 fs
nsteps = 200
friction = 0.02           # ps⁻¹ (typical)

# Langevin dynamics, start at 300 K
dyn = Langevin(atoms, dt, temperature=300.0, friction=friction)

# Temperature ramp 300 K → 600 K
for step in range(1, nsteps + 1):
    T_target = 300.0 + (600.0 - 300.0) * (step / nsteps)
    dyn.set_temperature(T_target)
    dyn.run(1)                     # one MD step
    if step % 50 == 0:
        print(f"Step {step:3d}: T = {atoms.get_temperature():6.2f} K "
              f"(target {T_target:6.1f} K)")
