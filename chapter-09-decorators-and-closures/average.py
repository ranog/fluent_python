# Example 9-8. average.py: a higher-order function to calculate a running average
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


# Example 9-9. Testing Example 9-8
avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(15))


# Example 9-10. Inspecting the function created by make_averager in Example 9-8
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

# Example 9-11. Continuing from Example 9-9
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
