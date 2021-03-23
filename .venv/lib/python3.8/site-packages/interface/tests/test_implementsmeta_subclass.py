from interface.interface import ImplementsMeta, implements, Interface


class ImplementsMetaSubclass(ImplementsMeta):

    def __new__(mcls, name, bases, clsdict):
        return super(ImplementsMetaSubclass, mcls).__new__(
            mcls, name, bases, clsdict,
        )


class MyInterface(Interface):  # pragma: nocover

    def method1(self, x, y):
        pass

    def method2(self, x, y, z):
        pass


def test_implementsmeta_subclass():
    class Impl(implements(MyInterface)):  # pragma: nocover
        @staticmethod
        def method1(x, y):  # swapped
            pass

        def method2(self, x, y, z):
            pass
