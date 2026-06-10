from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

# Create 2x2x2 FCC Al supercell
atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

# Convert 10 GPa to eV/Ang^3
pressure = 10 * units.GPa

# NPT MD setup
md = NPTBerendsen(atoms, timestep=1.0*units.fs, temperature=500, 
                  pressure=pressure, ttime=25*units.fs, 
                  pfactor=0.625*1000*units.GPa*units.fs**2)

# Print initial volume
print(f'Initial volume: {atoms.get_volume():.2f} Ang^3')

# Run 100 steps
md.run(steps=100)

# Print final volume
print(f'Final volume: {atoms.get_volume():.2f} Ang^3')
