import warnings

def division(a, b):
    if abs(b) < 0.01:
        warnings.warn("Warning: dividing by a number close to zero", UserWarning)
        return a / b

# Проверка различных фильтров
warnings.simplefilter("always")
print(division(10, 0.001))

warnings.simplefilter("ignore")
print(division(10, 0.001))

warnings.simplefilter("error")
print(division(10, 0.001))