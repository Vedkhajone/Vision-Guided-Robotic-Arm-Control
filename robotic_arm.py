import numpy as np

class RoboticArm:
    def __init__(self, link_lengths):
        self.link_lengths = link_lengths  # List of link lengths
        self.joint_angles = [0 for _ in link_lengths]  # Initialize joint angles to 0

    def forward_kinematics(self):
        """Compute (x, y) positions of each joint and the end effector."""
        positions = [(0, 0)]  # Start at the base
        x, y = 0, 0
        angle_sum = 0
        for i, (L, theta) in enumerate(zip(self.link_lengths, self.joint_angles)):
            angle_sum += np.radians(theta)
            x += L * np.cos(angle_sum)
            y += L * np.sin(angle_sum)
            positions.append((x, y))
        return positions

    def inverse_kinematics(self, target_x, target_y):
        """Compute joint angles (theta1, theta2) for a 2-link arm to reach (x, y)."""
        L1, L2 = self.link_lengths
        D = (target_x**2 + target_y**2 - L1**2 - L2**2) / (2 * L1 * L2)

        if np.abs(D) > 1:
            return None  # Target is unreachable

        theta2 = np.degrees(np.arccos(D))
        theta1 = np.degrees(np.arctan2(target_y, target_x) - np.arctan2(L2 * np.sin(np.radians(theta2)), L1 + L2 * np.cos(np.radians(theta2))))

        self.joint_angles = [theta1, theta2]
        return self.joint_angles
