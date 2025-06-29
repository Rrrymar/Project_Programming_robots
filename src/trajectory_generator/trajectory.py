import numpy as np

class TrajectoryGenerator:
    def __init__(self, q_start, q_end, steps):
        self.steps = steps
        t = np.linspace(0, 1, steps)
        self.q = np.zeros((steps, len(q_start)))
        for i in range(len(q_start)):
            A = q_end[i] - q_start[i]
            w = 2 * np.pi
            self.q[:, i] = q_start[i] + A * (np.sin(w * t) + 0.2 * np.sin(5 * w * t) + 0.05 * np.random.randn(steps))
        self.qd = np.gradient(self.q, axis=0)
        self.qdd = np.gradient(self.qd, axis=0)
