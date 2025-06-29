import numpy as np
import roboticstoolbox as rtb
from robot_definition.ur3_robot import UR3
from trajectory_generator.trajectory import TrajectoryGenerator
from visualization.plot_animation import plot_trajectory_comparison, plot_joint_angles_comparison

robot = UR3()
print(robot)

# Параметры для генерации траектории
q_start = np.array([0, -np.pi/2, np.pi/2, 0, 0, 0])
q_end = np.array([np.pi/2, -np.pi/3, np.pi/3, np.pi/4, np.pi/2, 0])
steps = 60

# Генерация траектории
traj_gen = TrajectoryGenerator(q_start, q_end, steps)
q_plan = traj_gen.q.copy()
q_hist = traj_gen.q.copy()

# Коррекция конфигураций
qlim = robot.qlim
invalid_frames = []

for i, q in enumerate(q_hist):
    if np.any(q < qlim[0]) or np.any(q > qlim[1]):
        invalid_frames.append(i)
        q_hist[i] = np.clip(q, qlim[0], qlim[1])

print(f"Found and fixed {len(invalid_frames)} invalid configurations")

# Расчет координат для траекторий
def calculate_ee_positions(q_traj):
    positions = np.zeros((len(q_traj), 3))
    for i, q in enumerate(q_traj):
        T = robot.fkine(q)
        positions[i] = T.t
    return positions

xyz_plan = calculate_ee_positions(q_plan)
xyz_actual = calculate_ee_positions(q_hist)

# Визуализация сравнения траекторий
plot_trajectory_comparison(xyz_plan, xyz_actual)
plot_joint_angles_comparison(q_plan, q_hist)
