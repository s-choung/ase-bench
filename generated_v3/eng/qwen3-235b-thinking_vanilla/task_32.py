from ase import Atoms
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import math

angle = 104.5 * math.pi / 180
d = 0.957
water = Atoms('HOH',
             positions=[(0, 0, 0),
                       (d * math.sin(angle/2), -d * math.cos(angle/2), 0),
                       (-d * math.sin(angle/2), -d * math.cos(angle/2), 0)],
             cell=[10, 10, 10],
             pbc=False)

calc = LennardJones(species=['O', 'H'], sigma=[0.8, 0.9], epsilon=[0.5, 0.5], rc=5.0, cutoff=5.0)
water.calc = calc

opt = BFGS(water)
opt.run(fmax=0.001)

vib = Vibrations(water, nfree=2)
vib.run()
for i, (freq, energy) in enumerate(zip(vib.get_frequencies(), vib.get_energies())):
    if freq > 0:
        print(f"Mode {i+1}: frequency = {freq:.2f} cm^-1, energy = {energy:.6f} eV")
    else:
        print(f"Mode {i+1}: imaginary frequency = {freq:.2f} cm^-1")
