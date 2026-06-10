from ase import Atoms
from ase.build import bulk
from ase.md.nvtberendsen import NVTBerendsen
from ase.calculators.lj import LennardJones
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = LennardJones()

atoms.set_momenta(atoms.get_masses() * 300 * units.kB)

dyn = NVTBerendsen(atoms, timestep=5 * units.fs, temperature_K=500, taut=0.5 * units.fs)

for i, _ in enumerate(dyn.irun(200)):
    if (i + 1) % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {i+1}: {temp:.2f} K")
