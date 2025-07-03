import numpy as np 
import os, sys 
import skvideo.io 
import matplotlib.pyplot as plt 
import gymnasium as gym
from stable_baselines3 import SAC
from stable_baselines3.common.logger import configure
from stable_baselines3.common.callbacks import CheckpointCallback
import warnings
warnings.filterwarnings('ignore')

output_path = SET_THE_PATH_TO_THE_OUTPUT_FOLDER
os.makedirs(output_path, exist_ok=True)
env_name = PUT_YOUR_ENVIRONMENT_NAME_HERE
env = gym.make(env_name, terminate_when_unhealthy=True, render_mode='rgb_array')
model = SAC(env=env, policy='MlpPolicy', verbose=1, gamma=0.99)
model.set_logger(configure(os.path.join(output_path, f'results_training')))
model.learn(total_timesteps=5e6, log_interval=4)


# The code below generates 1 and saves video of the final behavior
frames = []
obs,_ = env.reset()
frames.append(env.render())
for _ in range(1000):
    action, _ = model.predict(obs, deterministic=True)
    obs,_,_,_,_ = env.step(action)
    frames.append(env.render())

mat_video = np.array(frames)
skvideo.io.vwrite(os.path.join(output_path,'video_constrained_seed.mp4'), mat_video, outputdict={"-pix_fmt":"yuv420p"})
