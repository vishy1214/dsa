class myclass:
    #Closure
    addend = 10
    def make_adder_as_closure(arg):
        def add(addend,_arg = arg):
            return addend + _arg
        return add

    #bounded methods & callable intances are richer than the closures
    def make_add_as_bound_method(arg):
        class Adder:
            def __init__(self,arg):
                self._arg = arg

            def add(self,addend):
                return addend + self._arg

        return Adder(arg).add

    def make_adder_as_callable_interface(arg):
        class Adder:
            def __init__(self,arg):
                self._arg = arg

            def __call__(self, addend):
                return addend + self._arg

        return Adder(arg)