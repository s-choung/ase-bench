from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

mol = molecule('H2O')
mol.calc = EMT()
BFGS(mol).run(fmax=0.01)
vib = Vibrations(mol)
vib.run()
freqs = vib.get_frequencies()
ens = vib.get_energies()
for i, (f, e) in enumerate(zip(freqs, ens), 1):
    print(f"Mode {i}: {f:.2f} cm^-1, {e:.6f} eV")
vib.clean()
