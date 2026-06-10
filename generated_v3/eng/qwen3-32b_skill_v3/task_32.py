from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.05)
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()
energies = vib.get_energies()
for i, (f, e) in enumerate(zip(frequencies, energies)):
    print(f"Mode {i+1}: {f:.2f} cm⁻¹, {e:.6f} eV")
