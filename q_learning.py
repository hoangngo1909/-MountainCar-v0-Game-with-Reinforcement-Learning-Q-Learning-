import gym
import pyglet

# Tạo biến môi trường
env = gym.make("MountainCar-v0")
env.reset()

# Lấy State hiện tại sau khởi tạo
print(env.state)
# # Show môi trường
# env.render()
# input()

# Lấy số action mà xe có thể thực hiện
print (env.action_space.n)

# Lấy x tối thiểu, tối đa và vận tốc tối thiểu, tối đa
print(env.observation_space.high)
print(env.observation_space.low)

# # Render thử
# while True:
#     action = 2 # Thử luôn đi về bên phải
#     #env.step(action)
#     new_state, reward, done, _ = env.step(action)
#     print("Neu_state = {}, reward = {}".format(new_state, reward))
#     env.render()