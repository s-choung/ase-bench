from ase import Atoms
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
from ase.neb.interpolator import IDPPInterpolator

atoms = fcc111('Cu', size=(4, 4, 3), vacuum=10.0)
adatom = molecule('Cu')
adatom.center(vacuum=10.0, axis='z')

initial = atoms.copy()
initial.add_atom(adatom, position=(1.5, 1.5, 3.0)) #fcc hollow site

final = atoms.copy()
final.add_atom(adatom, position=(2.8, 0.0, 3.0)) #hpc hollow site

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.add_atom(adatom, position=img.positions[-1]) #keep atom consistent
    img.calc = EMT()  # Set calculator for each image

neb = NEB(images, interpolator=IDPPInterpolator())
neb.interpolate()

opt = BFGS(neb)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
energy_barrier = max(energies) - energies[0]

print(f"Energy barrier: {energy_barrier} eV")
