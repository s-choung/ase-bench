from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.001)
vib = Vibrations(atoms, nfree=2)
vib.run()
freqs = vib.get_frequencies()
for i, f in enumerate(freqs):
    e_eV = abs(f) * units.invcm
    print(f"Mode {i+1}: {f:.2f} cm^-1, {e_eV:.6f} eV")
vib.clean()
