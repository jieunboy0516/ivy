# import ivy
#
# ivy.set_backend("jax")
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
# transpiled_func = ivy.transpile(test_fn, to="ivy", args=(x1,))
#
# # import os
# # import sys
# #
# # compilerpath = (os.path.join( os.path.dirname(os.path.abspath(__file__)),\
#   ".." , "/ivy/ivy/compiler" ) )
# # os.chdir(compilerpath)
# # # print(os.getcwd())
# # sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), ".." ,\
#   "/ivy/ivy/compiler" ))
# # from _compiler import compile as _compile
