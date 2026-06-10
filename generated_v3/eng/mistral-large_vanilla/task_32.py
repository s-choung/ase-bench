from ase import Atoms
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT

h2o = Atoms('H2OH', positions=[[0, 0, 0], [0.76, 1.0, 0], [0, 0, 1.0]])
h2o.center(vacuum=5)
h2o.calc = EMT()

vib = Vibrations(h2o)
vib.run()
vib.summary()

for mode in range(3 * len(h2o)):
    freq_cm = vib.get_frequencies()[mode]
    energy_ev = vib.get_energies()[mode]
    if freq_cm > 0:
        print(f"Mode {mode}: {freq_cm:.2f} cm^-1, {energy_ev:.4f} eV")
