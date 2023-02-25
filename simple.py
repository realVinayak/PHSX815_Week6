




def rectange_rule(funct_to_evaluate, min_value, max_value, N_meas):
    step_size = (max_value - min_value)/N_meas
    integral = 0
    prev_val = min_value
    for index in range(N_meas):
        integral += funct_to_evaluate([prev_val])[0]
        prev_val += step_size
    return integral*step_size

def simple(min_limit, max_limit, N_inter, func_to_evaluate):
    return rectange_rule(func_to_evaluate, min_limit, max_limit, N_inter)
