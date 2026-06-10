from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms(
    'H2O',
    positions=[
        (0.000, 0.000, 0.000),
        (0.958, 0.000, 0.000),
        (-0.239, 0.927, 0.000),
    ],
)
atoms.calc = EMT()

e_before = atoms.get_potential_energy()
print(f"Energy before optimization: {e_before:.6f} eV")

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.02)

e_after = atoms.get_potential_energy()
print(f"Energy after optimization: {e_after:.6f} eV")
