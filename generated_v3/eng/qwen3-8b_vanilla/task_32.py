from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

water = molecule('H2O')
water.set_calculator(EMT())
vib = Vibrations(water)
vib.run()
frequencies = vib.get_frequencies()
for freq in frequencies:
    cm = freq * 8065.54429
    print(f"{cm:.2f} cm^-1, {freq:.2f} eV")
