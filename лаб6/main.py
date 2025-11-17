from cache_result import cache_result

@cache_result
def test(a, b):
    return a + b

print(test(5, 3))
print(test(5, 3))
