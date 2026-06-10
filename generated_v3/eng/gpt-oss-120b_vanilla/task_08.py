from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# N2 molecule (bond length ~1.10 Å)
n2 = Atoms('N2', positions=[[0, 0, -0.55], [0, 0, 0.55]])
n2.calc = EMT()

# Geometry optimization
BFGS(n2, logfile=None).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(n2, name='n2_vib')
vib.run()
vib.summary()                     # prints frequencies in THz
freq_THz = vib.get_frequencies()  # array of frequencies (THz)

# Convert to cm⁻¹ (1 THz = 33.35641 cm⁻¹)
freq_cm1 = freq_THz * 33.35641
print('Vibrational frequencies (cm⁻¹):')
for f in freq_cm1:
    print(f'{f:.2f}')

vib.clean()  # remove temporary files
