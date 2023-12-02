print("hello")
import numpy as np
print(np.__version__)
# from scipy.integrate import solve_ivp
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import struct
# import sys

# def lorenz(t, xyz, sigma, rho, beta):
#     x, y, z = xyz
#     dxdt = sigma * (y - x)
#     dydt = x * (rho - z) - y
#     dzdt = x * y - beta * z
#     return [dxdt, dydt, dzdt]

# def get_lorenz_solution(sigma, rho, beta, initial_conditions, t_span):
#     t_eval = np.linspace(t_span[0], t_span[1], 10000)

#     sol = solve_ivp(lorenz, t_span, initial_conditions, args=(sigma, rho, beta), t_eval=t_eval)

#     return sol.y[:, 1:].flatten()

# def plot_lorenz_attractor(solution, output_file):
#     x, y, z = np.split(solution, 3)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot(x, y, z, lw=0.5)
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.set_zlabel('Z-axis')
#     ax.set_title('Lorenz Attractor')

#     plt.savefig(output_file, format='png')

# sigma = 10.0
# rho = 28.0
# beta = 8.0 / 3.0

# t_span = (0, 25)

# initial_conditions = [sys.argv[1],sys.argv[2],sys.argv[3]]

# lorenz_solution = get_lorenz_solution(sigma, rho, beta, initial_conditions, t_span)
# output_file = sys.argv[5]
# plot_lorenz_attractor(lorenz_solution, output_file)


# # print("Flattened Lorenz Attractor Solution:")
# # print(lorenz_solution)
# # print("\n")


# result_array = [x % 32 for x in lorenz_solution]

# # print("Flattened Lorenz Attractor Solution(mod 32):")
# # print(result_array)
# # print("\n")

# def sum_binary_digits(fraction):
#     binary_representation = ''.join(f'{b:08b}' for b in struct.pack('>d', fraction))
#     digit_sum = sum(int(digit) for digit in binary_representation)
#     return digit_sum

# result_array = [sum_binary_digits(fraction)%2 for fraction in result_array]
# # print(result_array)


# def condense_array(arr, k):
#     n = 27000
#     arr = arr[:27000]
#     if n % k != 0:
#         print("Error: 10,000 is not divisible by k")
#         return
#     chunk_size = n // k

#     condensed_integers = []
#     for i in range(0, n, chunk_size):
#         chunk = arr[i:i+chunk_size]
#         condensed_integers.append(int(''.join(map(str, chunk)), 2))

#     return condensed_integers

# k = int(sys.argv[4])
# result_array = condense_array(result_array, k)
# print(result_array)