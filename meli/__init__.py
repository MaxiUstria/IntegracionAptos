class MeliClient:
    """Base Step is step super-class. Enforces the implementation of a launch method for
    polymorphic step behaviour."""

    def __init__(self):
        print("Launching {}!".format(self.__class__.__name__))

    def launch(self):
        raise NotImplementedError("All steps should implement a launch() method")
