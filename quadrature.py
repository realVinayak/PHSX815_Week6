from scipy import integrate



def quadrature(min_limit, max_limit, N_inter, func_to_evaluate):
    integral_result = integrate.quadrature(func_to_evaluate, min_limit, max_limit, miniter=N_inter, maxiter=N_inter)
    return integral_result[0]

