from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import MDLogger
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Create Cu FCC 3x3x3 supercell
a = 3.61  # lattice constant for Cu in Angstrom
atoms = Atoms('Cu', positions=[(0, 0, 0)])
atoms *= (3, 3, 3)
atoms.set_cell((a, a, a), scale_atoms=True)

# Set up calculator and MD
atoms.set_calculator(EMT())
dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature=300, taut=100*units.fs, taup=1000*units.fs, externalstress=1e5)

# Run MD simulation
log = MDLogger(dyn, logfile=None, header=True, stress=True, peratom=True)
dyn.attach(log, interval=1)
dyn.run(200)

# Print initial/final cell volume and pressure
initial_volume = atoms.get_volume()
final_volume = dyn.atoms.get_volume()
initial_pressure = dyn.log.final_pressure
final_pressure = dyn.log.final_pressure
print(f'Initial cell volume: {initial_volume} Angstrom^3, Initial pressure: {initial_pressure} GPa')
print(f'Final cell volume: {final_volume} Angstrom^3, Final pressure: {final_pressure} GPa')
