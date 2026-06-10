import numpy as np
from ase import units
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT

# Setup Al supercell
atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

# Unit conversion: 1 GPa = 10^9 Pa = 10^9 (N/m^2)
# 1 eV/Ang^3 = 1.60218e-19 J / (1e-10 m)^3 = 1.60218e-19 / 1e-30 = 1.60218e11 Pa
# Thus, 1 GPa = 1e9 / 1.60218e11 eV/Ang^3 approx 0.0062415 eV/Ang^3
pressure_gpa = 10.0
pressure_ev_ang3 = pressure_gpa * (1e9 / (units.pervo)) # units.pervo is 1 eV/Ang^3 in Pa

v_init = atoms.get_volume()

# MD setup
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# NPTBerendsen: timestep is in seconds, temperature in K, pressure in eV/Ang^3
# Note: ASE's NPTBerendsen expects pressure in units of eV/Ang^3 internally or based on units.fs
# Using the provided conversion logic for the simulation input
dyn = NPTBerendsen(atoms, timestep=1*units.fs, temperature_K=500, 
                  external_pressure=pressure_gpa * 1e9 / units.pervo, 
                  compressibility=4.5e-5) # approx Al compressibility

dyn.run(100)

v_final = atoms.get_volume()

print(f"Initial Volume: {v_init:.4f} Ang^3")
print(f"Final Volume:   {v_final:.4f} Ang^3")
print(f"Pressure (GPa to eV/Ang^3): {pressure_gpa} -> {pressure_gpa * 1e9 / units.pervo:.6f}")
