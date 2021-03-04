import abc


class AbstractTitle(abc.ABC):
    def __init__(self, **params):
        self.params = params

    @abc.abstractmethod
    def __repr__(self):
        pass


class Imports(AbstractTitle):
    def __repr__(self):
        return "\n".join(
            "from %s import %s" % (k, ', '.join(v))
            if v else
            "import %s" % k
            for k, v in self.params.items()
        )


class UpdateForwardRefs(AbstractTitle):
    def __repr__(self):
        return "\n" + "\n".join(
            '%s.update_forward_refs()' % k
            for k, _ in self.params.items()
        )
