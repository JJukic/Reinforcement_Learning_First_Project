import gymnasium as gym

# Create an environment
env = gym.make("CartPole-v1", render_mode="human")

# Reset environment to start a new episode
observation, info = env.reset()
# observation is what the agent can see - cart position, velocity, pole angle etc..
# info - debugging information

print(f"Observation started: {observation}")

episode_over = False
total_reward = 0

while not episode_over:
    # Interface mit dem Cart Pole
    env.render()

    # Choose an action: 0 = push the cart to left, 1 = push the cart to right
    action = env.action_space.sample() # Random action for now

    # Take the action
    observation, reward, terminated, truncated, info = env.step(action)

    # reward: +1 for each step pole stays upright
    # terminated: True if pole falls to far (agent failed)
    # truncated: True if we hit the time limit (500 steps)

    total_reward += reward
    episode_over = terminated or truncated

print(f"Episode over. Total reward: {total_reward}")
env.close()
