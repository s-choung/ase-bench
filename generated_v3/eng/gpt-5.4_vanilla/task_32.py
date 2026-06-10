from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='h2o_vib')
vib.run()

energies = vib.get_energies()
for i, e in enumerate(energies, 1):
    if abs(e.imag) > 1e-12:
        cm1 = e.imag / 0.0001239841984332003
        print(f"Mode {i:2d}: {cm1:10.2f}i cm^-1, {e.imag:10.6f}i eV")
    else:
        cm1 = e.real / 0.0001239841984332003
        print(f"Mode {i:2d}: {cm1:10.2f} cm^-1, {e.real:10.6f} eV")

vib.clean()
