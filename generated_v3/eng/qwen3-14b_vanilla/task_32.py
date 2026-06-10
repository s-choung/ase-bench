import math
from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

bond_length = 0.96
angle_deg = 104.5
angle = math.radians(angle_deg)
half_angle = angle / 2.0

x = bond_length * math.cos(half_angle)
z = bond_length * math.sin(half_angle)

positions = [
    (0.0, 0.0, 0.0),  # O
    (x, 0.0, z),       # H1
    (x, 0.0, -z)       # H2
]

atoms = Atoms('OHH', positions=positions)
atoms.set_calculator(EMT())

vib = Vibrations(atoms)
vib.calculate()

frequencies = vib.get_frequencies()
for i, freq in enumerate(frequencies):
    freq_cm = freq * 33.356
    energy_ev = freq * 0.0041357
    print(f"Mode {i+1}: {freq_cm:.2f} cm^-1, {energy_ev:.6f} eV")
