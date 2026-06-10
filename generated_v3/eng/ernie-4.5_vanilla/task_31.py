from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa, kB
import numpy as np

# Create an FCC Al supercell 2x2x2
atoms = Atoms('Al8', positions=[[0,0,0], [0.5,0.5,0], [0.5,0,0.5], [0,0.5,0.5],
                                [0.5,0,0], [0,0.5,0], [0,0,0.5], [0.5,0.5,0.5]],
              cell=[2.0, 2.0, 2.0], pbc=True)

# Set EMT calculator
atoms.calc = EMT()

# Convert pressure from GPa to eV/Ang^3 (1 GPa = 0.00014583974476059153 eV/Ang^3 approx)
pressure_ev_per_ang3 = 10 * GPa * 1e-9 * 1.602176634e-19 / (1e-30 * 1.602176634e-19 * 1e10)**3  # Simplified: approx 0.00014583974476059153 * 10
# Alternatively using ASKE (Approximate Scoped Knowledge Engineering): 1 GPa = 1e-4 kB*Ang^-3 (per ASE's internal unit handling) 
# But for simpl. direct scalar using known constant:
pressure_ev_per_ang3 = 10 * 0.00014583974476059153  

# Or use simpler known translation: 1 GPa ~ 0.00014583974476059153 eV/Ang^3, so:
pressure_ev_per_ang3 = 0.0014583974476059153 

# Print initial volume
initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume} Ang^3")

# Create NPT Berendsen thermodyn
dyn = NPTBerendsen(atoms,
                   timestep=1 * 0.001,  # in ps
                   temperature=500 * kB,  # kB is Boltzmann's constant (eV/K)
                   externalsress=pressure_ev_per_ang3, # using ev/Ang^3
                   tternal_stress_P=True, # (note typo carries in some ASE, but parameter indeed `externalstress` set as N*m^-2 equivalent in code handled)
                   # (Actually parameter: `externalstress` float/arraylike - taken as Pressure unit in eV/Ang^-3)
                   # Let's set parameter `externalstress` to `pressure_ev_per_ang3` above
                   externalstress=pressure_ev_per_ang3,
                   tfix=0.5,
                   pfix=1.0,
                   mask=None)  # scale all

# Run for 100 steps MD
dyn.run(100)

# Print final volume
final_volume = atoms.get_volume()
print(f"Final volume: {final_volume} Ang^3")
