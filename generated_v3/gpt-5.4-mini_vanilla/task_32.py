from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.units import invcm

atoms = Atoms('H2O', positions=[(0.0000, 0.0000, 0.0000),
                                (0.9572, 0.0000, 0.0000),
                                (-0.2390, 0.9270, 0.0000)])
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name='h2o_vib')
vib.run()

for i, mode in enumerate(vib.get_energies()):
    freq_cm1 = vib.get_frequencies()[i].real
    energy_ev = mode.real
    print(f"Mode {i+1}: {freq_cm1:.2f} cm^-1, {energy_ev:.6f} eV")

vib.clean()
