from ase import Atoms
from ase.geometry import interpolate
from ase.calculators.emt import EMT

initial = Atoms('Al3', positions=[[0,0,0], [2,0,0], [0.5,0,0]])
final = Atoms('Al3', positions=[[0,0,0], [2,0,0], [1.5,0,0]])
images = interpolate(initial, final, 2)

for img in images:
    img.set_calculator(EMT())

for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy()}")
