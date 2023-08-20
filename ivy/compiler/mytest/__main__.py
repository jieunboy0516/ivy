# import ivy
#
# ivy.set_backend("jax")
# print(__package__)
# # from _compiler.so import compile as _compile
#
#
# def test_fn(x):
#     return jax.numpy.sum(x)
#
#
# x1 = ivy.array([1.0, 2.0])
#
# print(ivy)
# # transpiled_func and unified_func will have the same result
#
# transpiled_func = ivy.transpile(test_fn, to="ivy", args=(x1,))
