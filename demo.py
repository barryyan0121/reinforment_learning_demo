import numpy as np


def point_cylinder_intersection(
    cylinder_base, cylinder_top, radius, points, threshold=0
):
    """
    检查圆柱体和点列表的交集。

    :param cylinder_base: 圆柱体底面中心点坐标，形如 [x, y, z]
    :param cylinder_top: 圆柱体顶面中心点坐标，形如 [x, y, z]
    :param radius: 圆柱体的半径
    :param points: 点的列表，形如 [[x1, y1, z1], [x2, y2, z2], ...]
    :param threshold: 与圆柱体表面的距离阈值
    :return: 布尔值列表，表示每个点是否与圆柱体相交
    """
    cylinder_axis = np.array(cylinder_top) - np.array(cylinder_base)
    intersections = []
    for point in points:
        point_vec = np.array(point) - np.array(cylinder_base)
        proj_length = np.dot(point_vec, cylinder_axis) / np.linalg.norm(cylinder_axis)
        if 0 <= proj_length <= np.linalg.norm(cylinder_axis):
            proj_point = np.array(cylinder_base) + proj_length * (
                cylinder_axis / np.linalg.norm(cylinder_axis)
            )
            distance = np.linalg.norm(np.array(point) - proj_point)
            intersections.append(distance <= radius + threshold)
        else:
            intersections.append(False)
    return intersections


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_cylinder_and_points(
    cylinder_base, cylinder_top, radius, points, intersections
):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    cylinder_base = np.array(cylinder_base)
    cylinder_top = np.array(cylinder_top)
    points = np.array(points)

    # 画圆柱体
    v = cylinder_top - cylinder_base
    v_length = np.linalg.norm(v)
    v = v / v_length
    not_v = np.array([1, 0, 0]) if v[0] == 0 else np.cross(v, [1, 0, 0])
    n1 = np.cross(v, not_v)
    n1 /= np.linalg.norm(n1)
    n2 = np.cross(v, n1)
    t = np.linspace(0, v_length, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    t, theta = np.meshgrid(t, theta)
    X, Y, Z = [
        cylinder_base[i]
        + v[i] * t
        + radius * np.sin(theta) * n1[i]
        + radius * np.cos(theta) * n2[i]
        for i in [0, 1, 2]
    ]
    ax.plot_surface(X, Y, Z, color="b", alpha=0.5)

    # 画点
    for i, point in enumerate(points):
        ax.scatter(*point, color="r" if intersections[i] else "g", s=100)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


# 测试数据和调用函数
cylinder_base = [0, 5, 10]
cylinder_top = [0, 0, 10]
radius = 2
points = [[1, 1, 5], [3, 3, 6], [5, 5, 15], [7, 7, 7]]
intersections = point_cylinder_intersection(
    cylinder_base, cylinder_top, radius, points, threshold=0
)
print(intersections)
plot_cylinder_and_points(cylinder_base, cylinder_top, radius, points, intersections)
