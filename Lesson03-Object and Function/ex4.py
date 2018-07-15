def maker(x):
    def action(y):
        return x**y
    return action

f = maker(9)
print(f(5))