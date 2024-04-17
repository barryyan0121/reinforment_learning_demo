import numpy as np
from tqdm import tqdm

# 定义环境
num_states = 5  # 状态数量
num_actions = 3  # 动作数量

# 初始化Q表
Q = np.zeros((num_states, num_actions))

# 定义参数
alpha = 0.1  # 学习率
gamma = 0.9  # 折扣因子
epsilon = 0.1  # 探索率

# 定义状态转移矩阵
R = np.array([[-1, -1, -1, -1, 0],
              [-1, -1, -1, 100, -1],
              [-1, -1, 0, -1, 100],
              [-1, 0, -1, -1, 0],
              [0, -1, 100, 0, 100]])


# 状态转移逻辑，这里假设状态转移仅基于当前状态和动作
def get_next_state(state, action):
    if state == 4:
        return 4  # Terminal state loops to itself
    elif state == 2 and action == 2:
        # Probabilistic transition from state 2 with action 2
        return np.random.choice([3, 4], p=[0.4, 0.6])  # 40% chance to go to state 3, 60% to go to state 4
    elif state == 3 and action == 1:
        # Probabilistic transition from state 3 with action 1
        return np.random.choice([4, 3], p=[0.7, 0.3])  # 70% chance to go to state 4, 30% to stay in state 3
    elif action == num_actions - 1:
        # Generally move forward, but with a chance to stay
        return np.random.choice([state + 1, state], p=[0.8, 0.2])  # 80% move forward, 20% stay
    else:
        if state == 0:
            return state  # Stay if already at the first state
        # Move backward or stay with some probability
        return np.random.choice([state - 1, state], p=[0.7, 0.3])  # 70% move back, 30% stay


# Q-Learning算法
def q_learning(state, Q, R, alpha, gamma, epsilon):
    # 选择动作
    if np.random.uniform(0, 1) < epsilon:
        action = np.random.randint(0, num_actions)  # 探索
    else:
        action = np.argmax(Q[state])  # 利用Q表选择最优动作

    # 状态转移
    next_state = get_next_state(state, action)

    # 更新Q值
    Q[state, action] += alpha * (R[state, action] + gamma * np.max(Q[next_state]) - Q[state, action])

    return next_state


def validate_policy(initial_state, num_steps, Q):
    state = initial_state
    best_path = []

    for _ in range(num_steps):
        if state == 4:  # Check if it's the terminal state
            action = np.argmax(Q[state])
            best_path.append((state, action))
            print("Reached terminal state.")
            break
        action = np.argmax(Q[state])  # Select the best action based on the learned Q-values
        best_path.append((state, action))
        state = get_next_state(state, action)  # Move to the next state

    return best_path


# 训练过程
num_episodes = 10000
for episode in tqdm(range(num_episodes), desc="Training", unit="episodes"):
    state = np.random.randint(0, num_states)  # 随机选择初始状态
    while state != 4:  # 直到达到终止状态
        state = q_learning(state, Q, R, alpha, gamma, epsilon)


# Example usage after training
initial_state = 0  # Start from state 0
num_steps = 10  # Max number of steps to simulate
best_path = validate_policy(initial_state, num_steps, Q)


# 输出训练后的Q表
print("Trained Q-table:")
print(Q)

# Print the best path
print("Best path based on learned Q-table:")
for state, action in best_path:
    print(f"State: {state}, Action: {action}")


