# import numpy as np
# from scipy.integrate import solve_ivp
# import matplotlib.pyplot as plt
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

# result_array = [x*10000 % 32 for x in lorenz_solution]

# def sum_binary_digits(fraction):
#     binary_representation = ''.join(f'{b:08b}' for b in struct.pack('>d', fraction))
#     digit_sum = sum(int(digit) for digit in binary_representation)
#     return digit_sum

# result_array = [sum_binary_digits(fraction)%2 for fraction in result_array]



# def condense_binary_array(binary_array):
#     condensed_array = []

#     for i in range(0, 800, 8):
#         binary_chunk = ''.join(map(str, binary_array[i:i+8]))
#         decimal_value = int(binary_chunk, 2)
#         condensed_array.append(decimal_value)

#     return condensed_array

# random_numbers = condense_binary_array(result_array)
# print(random_numbers)





import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import struct
from pypuf.simulation import XORArbiterPUF
from pypuf.io import random_inputs
import sys

def lorenz(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def get_lorenz_solution(sigma, rho, beta, initial_conditions, t_span):
    t_eval = np.linspace(t_span[0], t_span[1], 10000)

    sol = solve_ivp(lorenz, t_span, initial_conditions, args=(sigma, rho, beta), t_eval=t_eval)

    return sol.y[:, 1:].flatten()

def plot_lorenz_attractor(solution, output_file):
    x, y, z = np.split(solution, 3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, lw=0.5)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Lorenz Attractor')

    plt.savefig(output_file, format='png')

sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

t_span = (0, 25)

initial_conditions = [sys.argv[1],sys.argv[2],sys.argv[3]]
lorenz_solution = get_lorenz_solution(sigma, rho, beta, initial_conditions, t_span)
output_file = sys.argv[4]
plot_lorenz_attractor(lorenz_solution , output_file)

result_array = [x*10000 % 32 for x in lorenz_solution]

def sum_binary_digits(fraction):
    binary_representation = ''.join(f'{b:08b}' for b in struct.pack('>d', fraction))
    digit_sum = sum(int(digit) for digit in binary_representation)
    return digit_sum

result_array = [sum_binary_digits(fraction)%2 for fraction in result_array]

challenge_length = 64
puf = XORArbiterPUF(n=challenge_length, k=2)

chunks = [result_array[i:i+8] for i in range(0, len(result_array), 8)]
responses = []

for chunk in chunks:
    binary_element = ''.join(map(str, chunk))  
    seed = int(binary_element, 2)  
    puf.seed = seed  
    challenges = random_inputs(n=challenge_length, N=1, seed=seed)
    response = puf.eval(challenges)
    responses.append(response[0])

result_array = [0 if x == -1 else x for x in result_array]

def condense_binary_array(binary_array):
    condensed_array = []

    for i in range(0, 800, 8):
        binary_chunk = ''.join(map(str, binary_array[i:i+8]))
        decimal_value = int(binary_chunk, 2)
        condensed_array.append(decimal_value)

    return condensed_array

random_numbers = condense_binary_array(result_array)
print(random_numbers)
