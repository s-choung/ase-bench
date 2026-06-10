from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create 2x2x2 FCC Cu supercell and set calculator
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Print initial state
print(f"Initial temperature: {atoms.get_temperature():.1f} K")
print(f"Initial potential energy: {atoms.get_potential_energy():.3f} eV")

# Setup Langevin at 300 K with 5 fs timestep
dyn = Langevin(atoms, timestep=5 * units.fs,
               temperature_K=300, friction=0.01)

# Run 100 MD steps
dyn.run(100)

# Print final state
print(f"Final temperature: {atoms.get_temperature():.1f} K")
print(f"Final potential energy: {atoms.get_potential_energy():.3f} eV")
