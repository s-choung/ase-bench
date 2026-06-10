from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.units import _h, _e, _c

# H2O geometry (approximate)
atoms = Atoms('H2O',
              positions=[(0.0, 0.0, 0.0),
                         (0.757, 0.586, 0.0),
                         (-0.757, 0.586, 0.0)])

atoms.set_calculator(EMT())
BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name='h2o_vib')
vib.run()

freq_THz = vib.get_frequencies()                     # THz
c_cm = _c * 100                                      # cm·s⁻¹
freq_cm = freq_THz * 1e12 / c_cm                     # cm⁻¹
energy_eV = (_h * freq_THz * 1e12) / _e              # eV

for i, (f_cm, e_ev) in enumerate(zip(freq_cm, energy_eV), 1):
    if f_cm > 0:  # ignore imaginary (negative) frequencies
        print(f"Mode {i:2d}: {f_cm:8.2f} cm⁻¹  →  {e_ev:6.4f} eV")

vib.clean()
