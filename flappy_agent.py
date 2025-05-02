import gym
import numpy as np
import pygame
from gym import spaces
import flappy_bird_gym 

class FlappyBirdEnv(gym.Env):
    def __init__(self):
        super().__init__()
        
        self.env = flappy_bird_gym.make("FlappyBird-v0")

        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space

    def reset(self):
        return self.env.reset()

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        return obs, reward, done, info

    def render(self):
        self.env.render()

    def close(self):
        self.env.close()
