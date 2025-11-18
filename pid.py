"""Use a PID controller for CartPole.

When run, this will play an animation.
"""

import gym


DT = .02
KP = 1
KI = 1
KD = 1


class PID:
    def __init__(self):
        self._integral = 0
        self._prev_error = 0

    def reset(self):
        self._integral = 0
        self._prev_error = 0

    def compute(self, error):
        """Return the control signal."""
        self._integral += error * DT
        derivative = (error - self._prev_error) / DT
        self._prev_error = error

        return KP * error + KI * self._integral + KD * derivative

    

def main():
    env = gym.make('CartPole-v1')
    state = env.reset()
    pid = PID()
    for _ in range(1000):
        env.render()
        u = pid.compute(-state[2])
        action = 0 if u > 0 else 1
        state, _, done, _ = env.step(action)

        if done:
            state = env.reset()
            pid.reset()

    env.close()
        
        


if __name__ == '__main__':
    main()
