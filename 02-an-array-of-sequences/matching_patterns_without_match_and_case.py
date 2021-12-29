class Procedure():
    pass


def evaluate(x, env):
    "Evaluate an expression in an environment."
    if ...:
        # several lines omitted
        ...
    elif x[0] == 'quote':
        # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if':
        # (if test conseq alt)
        (_, test, consequence, alternative) = x
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif x[0] == 'define':
        # (define name exp)
        (_, name, exp) = x
        env[name] = evaluate(exp, env)
    elif x[0] == 'lambda':
        # (lambda (parm…) body)
        (_, parms, *body) = x
        return Procedure(parms, body, env)
