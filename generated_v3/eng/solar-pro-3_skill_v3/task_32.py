from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = Atoms('H2O')
atoms.calc = EMT()

# optimize geometry first
from ase.optimize import BFGS
BFGS(atoms, trajectory='opt.traj').run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

freqs = vib.get_frequencies()           # cm⁻¹
energies = vib.get_energies()           # eV

for i, fr in enumerate(freqs):
    print(f'Mode {i+1}:  {fr:.1f} cm⁻¹,  {energies[i]:.2f} eV')
vib.clean()
