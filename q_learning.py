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
              [-1, -1, -1, 0, -1],
              [-1, -1, 0, -1, 100],
              [-1, 0, -1, -1, 0],
              [0, -1, 100, 0, 100]])


# 状态转移逻辑，这里假设状态转移仅基于当前状态和动作
def get_next_state(state, action):
    if state == 2 and action == 2:
        return 4  # 直接到达终止状态
    elif action == num_actions - 1:
        return min(state + 1, num_states - 1)  # 向前移动到下一个状态
    else:
        return max(state - 1, 0)  # 向后移动到前一个状态


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


# 训练过程
num_episodes = 1000
for episode in tqdm(range(num_episodes)):
    state = np.random.randint(0, num_states)  # 随机选择初始状态
    while state != 4:  # 直到达到终止状态
        state = q_learning(state, Q, R, alpha, gamma, epsilon)

# 输出训练后的Q表
print("Trained Q-table:")
print(Q)
