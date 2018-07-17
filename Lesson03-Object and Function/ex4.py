def maker(x):
    def action(y):
        return x**y
    return action

f = maker(8)
print(f(4))