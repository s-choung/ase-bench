from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = Atoms('H2O', positions=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])
atoms.calc = EMT()
vib = Vibrations(atoms)
vib.run()
vib.write_mode()
for mode in vib.get_modes():
    print(f"Frequency: {mode.get_frequency()*-1*21433.4647:.2f} cm^-1, Energy: {mode.get_energy():.4f} eV")
