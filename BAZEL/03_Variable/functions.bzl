"""
Module doc string
"""
def _foo_binary_impl(ctx):
    a = [1,2,3]
    print("analyzing", ctx.label ,a , len(a))

foo_binary = rule(
    implementation = _foo_binary_impl,
)

print("bzl file evaluation")