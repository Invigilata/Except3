import warnings

def division_calculation(dividend, divisor):
    if abs(divisor) < 0.01:
        warnings.warn("Warning: Divider is close to zero", UserWarning)

        return dividend / divisor

# Different filters: always, ignore, error
warnings.simplefilter("always")
result = division_calculation(10, 0.001)

warnings.simplefilter("ignore")
result = division_calculation(20, 0.001)

try:
    warnings.simplefilter("error")
    result = division_calculation(30, 0.001)
except UserWarning as e:
    print(f"Caught UserWarning: {e}")