from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.berendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Build Cu 3x3x3 FCC supercell
cu = bulk('Cu', 'fcc') * (3, 3, 3)
cu.calc = EMT()

# Initialize velocities and get initial state
MaxwellBoltzmannDistribution(cu, temperature_K=300)
cu.get_forces()
init_vol = cu.get_volume()
init_press = cu.get_pressure() * (units.eV / units.A**3) / units.bar

# Set up NPT Berendsen (Cu isothermal compressibility ~4.5e-38 A³/eV)
npt = NPTBerendsen(cu, temperature_K=300, pressure=1*units.bar,
                   taut=100*units.fs, taup=1000*units.fs,
                   compressibility=4.5e-38)
dyn = VelocityVerlet(cu, timestep=5*units.fs)
dyn.attach(npt)

# Run MD
dyn.run(200)

# Get final state
cu.get_forces()
fin_vol = cu.get_volume()
fin_press = cu.get_pressure() * (units.eV / units.A**3) / units.bar

# Print results
print(f'Initial: Vol={init_vol:.2f} A³, Press={init_press:.2f} bar')
print(f'Final:   Vol={fin_vol:.2f} A³, Press={fin_press:.2f} bar')
