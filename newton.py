def first_derivative(f, x, eps = 0.00001):
    return (f(x+eps)-f(x-eps))/2/eps

def second_derivative(f, x, eps = 0.00001):
    return (f(x+eps)-2*f(x)+f(x-eps))/eps**2

def my_newton_method(x0, f, tol = 0.000001, max_count = 100000):
    # for robustness
    count = 0
    x = x0 - first_derivative(f, x0)/second_derivative(f, x0) # to run the while loop
    while abs(f(x) - f(x0)) > tol and count < max_count:
        x0 = x
        x = x0 - first_derivative(f, x0)/second_derivative(f, x0)
        count += 1
        print(count, x)
    if abs(f(x) - f(x0)) <= tol:
        return x
    else:
        raise ValueError("Max count of {} is reached and it still can't converge".format(max_count))