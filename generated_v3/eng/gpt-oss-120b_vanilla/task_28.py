from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# ----- Create Cu FCC 2x2x2 supercell -----
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
atoms.set_temperature(300)                     # initial velocities

# ----- MD parameters -----
timestep = 5 * units.fs                         # 5 fs
nsteps   = 200
temp_start = 300.0                              # K
temp_end   = 600.0                              # K
friction   = 0.02                               # 1/ps (ASE internal units)

# ----- Langevin dynamics -----
dyn = Langevin(atoms, timestep, temperature_K=temp_start,
               friction=friction, logfile=None)

# ----- Run with linear temperature ramp -----
for step in range(nsteps):
    # linear interpolation of temperature
    target_T = temp_start + (temp_end - temp_start) * step / nsteps
    dyn.temperature = target_T                 # update thermostat

    dyn.run(1)                                 # single integration step

    if step % 50 == 0:
        # instantaneous kinetic temperature
        kin_T = atoms.get_temperature()
        print(f"Step {step:3d}: Target T = {target_T:6.1f} K, "
              f"Instantaneous T = {kin_T:6.1f} K")
