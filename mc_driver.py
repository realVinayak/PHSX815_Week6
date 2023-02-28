import random
from driver import func_to_evaluate, integral_result_analytic
from quadrature import quadrature

N_sample = 4000
MIN_X = 3.2
MAX_X = 6
MIN_Y = -25
MAX_Y = 0


def mc_driver(func_to_evaluate_main, sample_gen, min_x, max_x, min_y, max_y):
    integral_value = 0
    for counter in range(N_sample):
        sample = sample_gen()
        sample_x = sample[0]
        func_at_x = func_to_evaluate_main([sample_x])[0]
        contains = False
        if func_at_x * sample[1] >= 0:
            contains = abs(func_at_x) >= abs(sample[1])
        if contains:
            integral_value += 1
    return (integral_value / N_sample) * (max_y - min_y) * (max_x - min_x)


def sample_gen_func(min_x, max_x, min_y, max_y):
    random_x = random.random() * (max_x - min_x) + min_x
    random_y = random.random() * (max_y - min_y) + min_y
    return random_x, random_y


def main():
    mc_result = abs(mc_driver(func_to_evaluate,
                    lambda: sample_gen_func(MIN_X, MAX_X, MIN_Y, MAX_Y), MIN_X,
                    MAX_X, MIN_Y, MAX_Y))
    quad_result = abs(quadrature(MIN_X, MAX_X, N_sample, func_to_evaluate))
    analytic_result = abs(integral_result_analytic(MAX_X) - integral_result_analytic(MIN_X))
    print('Monte Carlo Result: ', mc_result)
    print('Quadrature Result: ', quad_result)
    print('Analytic Result: ', analytic_result)
    print('Error in Monte Carlo Result: ', abs(mc_result - analytic_result))

if __name__ == '__main__':
    main()
