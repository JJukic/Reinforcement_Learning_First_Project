import gymnasium as gym

# Create an environment
env = gym.make("CartPole-v1")

# Reset environment to start a new episode
observation, info = env.reset()
# observation is what the agent can see - cart position, velocity, pole angle etc..
# info - debugging information


