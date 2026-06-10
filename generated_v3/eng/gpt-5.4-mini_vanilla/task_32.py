from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.units import invcm

# H2O molecule
atoms = Atoms(
    "OH2",
    positions=[
        (0.0000, 0.0000, 0.0000),
        (0.9584, 0.0000, 0.0000),
        (-0.2396, 0.9271, 0.0000),
    ],
)

atoms.calc = EMT()

# Relax geometry
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

# Vibrations
vib = Vibrations(atoms, name="h2o_vib")
vib.run()

modes = vib.get_energies()  # eV
freqs_cm1 = modes / invcm

for i, (f, e) in enumerate(zip(freqs_cm1, modes), 1):
    print(f"Mode {i:2d}: {f:12.3f} cm^-1   {e:12.6f} eV")

vib.clean()
