import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def plot_trajectory_comparison(xyz_plan, xyz_actual):
    fig = plt.figure(figsize=(12, 10))
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot(xyz_plan[:, 0], xyz_plan[:, 1], xyz_plan[:, 2], 'r--', label='Planned Trajectory', linewidth=2)
    ax1.plot(xyz_actual[:, 0], xyz_actual[:, 1], xyz_actual[:, 2], 'b-', label='Actual Trajectory', linewidth=2)
    ax1.scatter(xyz_plan[0, 0], xyz_plan[0, 1], xyz_plan[0, 2], c='g', s=80, label='Start')
    ax1.scatter(xyz_plan[-1, 0], xyz_plan[-1, 1], xyz_plan[-1, 2], c='r', s=80, label='End')
    ax1.set_title('End-Effector Trajectory Comparison')
    ax1.set_xlabel('X (m)')
    ax1.set_ylabel('Y (m)')
    ax1.set_zlabel('Z (m)')
    ax1.legend()
    plt.show()

def plot_joint_angles_comparison(q_plan, q_hist):
    fig = plt.figure(figsize=(12, 8))
    ax2 = fig.add_subplot(122)
    for i in range(6):
        ax2.plot(q_plan[:, i], '--', label=f'Joint {i+1} (planned)', linewidth=2)
        ax2.plot(q_hist[:, i], '-', label=f'Joint {i+1} (actual)', linewidth=2)
    ax2.set_title('Joint Angles Comparison')
    ax2.set_xlabel('Step')
    ax2.set_ylabel('Joint Angle (rad)')
    ax2.grid(True)
    ax2.legend()
    plt.tight_layout()
    plt.savefig('trajectory_comparison.png')
    plt.show()
