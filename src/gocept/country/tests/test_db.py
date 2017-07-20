from gocept.country.db import Data


def test_db__Data____hash____():
    """It implements a hash method.

    This is requested for Python 3 as `Data` implements `__eq__`.
    """
    assert hash(Data('foo')) is not None
