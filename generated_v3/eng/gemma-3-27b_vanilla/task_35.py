from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import nudged_elastic_band
from ase.io import write

a = 3.6
initial = molecule('AlAl', geometry='linear', a=a)
final = molecule('AlAl', geometry='linear', a=a)
final.positions[1] += [0, 0, a]

images = [initial, final]

neb = nudged_elastic_band(images, EMT())

calc = EMT()
for i, image in enumerate(neb):
    image.set_calculator(calc)
    energy = image.get_potential_energy()
    print(f"Image {i+1} Energy: {energy} eV")
