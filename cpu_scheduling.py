import math


def calculate_cpu_usage(tasks):
    if not tasks:
        return []

    # 找到最后一个任务的结束时间
    max_time = 0
    for start, end, _ in tasks:
        max_time = max(max_time, end)

    # 初始化CPU使用率数组
    intervals = math.ceil(max_time / 5)  # 确定需要多少个5秒间隔
    cpu_usage = [0] * intervals
    count = [0] * intervals  # 存储每个区间的任务计数器

    # 更新每个任务对应的区间
    for start, end, usage in tasks:
        start_index = start // 5
        end_index = (end // 5)
        for i in range(start_index, end_index):
            cpu_usage[i] += usage
            count[i] += 1

    # 计算每个区间的平均CPU使用率
    average_usage = []
    for i in range(intervals):
        if count[i] > 0:
            average_usage.append(cpu_usage[i] / count[i])
        else:
            average_usage.append(0)  # 如果没有任务，则CPU使用率为0

    return average_usage


# 示例任务数据
tasks = [
    (0, 5, 100),  # 任务1：从0到5秒，CPU占用率为100%
    (1, 6, 50),  # 任务2：从1到6秒，CPU占用率为50%
    (10, 15, 30)  # 任务3：从10到15秒，CPU占用率为30%
]

# 调用函数并打印结果
print(calculate_cpu_usage(tasks))
