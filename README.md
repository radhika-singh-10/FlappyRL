# FlappyRL

## Autonomous Gameplay in Flappy Bird Using Deep Reinforcement Learning

The use of Reinforcement Learning (RL) in a Flappy Bird game is mainly to train an agent (the bird) to learn by itself how to maximize survival and score points by flapping or not flapping at each moment, without hardcoding rules.


## Installation

1. Clone the repository:
    ```bash
    https://github.com/radhika-singh-10/FlappyRL.git
    ```

2. Navigate to the project directory:
    ```bash
    cd FlappyRL
    ```

3. Create a virtual environment and install the dependencies:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

   
## Usage

To test the game, run the following command:
```bash
python game.py
```

To test the environment, run the following command:
```bash
python env.py
```

To train the reinforcement learning agent, run the following command:
```bash
python agent.py --train --model-type ppo
```
