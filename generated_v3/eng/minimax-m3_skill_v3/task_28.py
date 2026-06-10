from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

T_start, T_end, n_steps = 300, 600, 200
dyn = Langevin(atoms, timestep=5 * units.fs,
               temperature_K=T_start, friction=0.01 / units.fs)

print(f"{'Step':>6} {'Target_T(K)':>12} {'Current_T(K)':>14}")
for step in range(n_steps + 1):
    T_target = T_start + (T_end - T_start) * step / n_steps
    if step % 50 == 0:
        print(f"{step:6d} {T_target:12.2f} {atoms.get_temperature():14.2f}")
    if step < n_steps:
        T_next = T_start + (T_end - T_start) * (step + 1) / n_steps
        dyn.set_temperature(T_next)
        dyn.run(1)
