from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

h2o = Atoms('H2O',
            positions=[[0.7575, 0.5870, 0.0],
                       [-0.7575, 0.5870, 0.0],
                       [0.0, 0.0, 0.0]])
h2o.calc = EMT()

BFGS(h2o).run(fmax=0.01)

vib = Vibrations(h2o)
vib.run()

energies = vib.get_energies()
frequencies = vib.get_frequencies()

for i, (e, f) in enumerate(zip(energies, frequencies)):
    print(f"Mode {i}: {f.real:.2f} cm^-1, {e.real:.6f} eV")

vib.clean()
