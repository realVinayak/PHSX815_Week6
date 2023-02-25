from quadrature import quadrature
from simple import simple
import math

min_limit = 4
max_limit = 7
N_inter = 300

def func_to_evaluate(y):
    return [(x**2)*(math.sin(x)) for x in y]

def integral_result_analytic(x):
    return 2*x*math.sin(x) + (2-(x**2))*math.cos(x)

def driver():
    simple_result = simple(min_limit, max_limit, N_inter, func_to_evaluate)
    quad_result = quadrature(min_limit, max_limit, N_inter, func_to_evaluate)
    expected_result = integral_result_analytic(max_limit)-integral_result_analytic(min_limit)
    print('result using fixed interval: ', simple_result)
    print('error using fixed interval: ', (abs(simple_result - expected_result)))
    print('result using quadrature method: ', quad_result)
    print('error using quadrature method: ', (abs(quad_result - expected_result)))
    print('result analytically: ', expected_result)

if __name__ == '__main__':
    driver()