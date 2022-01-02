class Symbol:
    pass


class Procedure:
    pass


def evaluate(exp, env):
    """Evaluate an expression in an environment."""
    match exp:
        # case ...:
        #     several lines omitted
        #     ...
        case ['quote', exp]:
            return exp
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['define', Symbol(name), exp]:
            env[name] = evaluate(exp, env)
        case ['define', [Symbol(name), *parms], *body] if body:
            env[name] = Procedure(parms, body, env)
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        # more lines omitted
        case _:
            raise SyntaxError(repr(exp))
