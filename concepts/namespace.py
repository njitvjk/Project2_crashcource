# Note: You may get different values for the id

value_a = 2
print('id(value_a) =', id(value_a))
value_a = value_a + 1
print('id(value_a) =', id(value_a))
value_b = 2
print('id(b) =', id(value_b))


# ===================defining scope======================
def namespace_scope_example():
    # local scope
    print("============scopes==================")
    a = 20

    def namespace_scope_example_local():
        # nested local scope
        a = 30
        print('a =', a)

    namespace_scope_example_local()
    print('a =', a)


# global scope
a = 10
namespace_scope_example()
print('a =', a)

# =========================================================




