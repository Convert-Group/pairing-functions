# -*- coding: utf-8 -*-

import pytest

from pairing_functions.szudzik import pair, unpair


class TestSzudzikPairing(object):

    def test_pair(self) -> None:

        assert pair(0, 0) == 0
        assert pair(0, 1) == 1
        assert pair(1, 0) == 2
        assert pair(2, 2) == 8
        assert pair(3, 4) == 19
        assert pair(92, 23) == 8579

    def test_pair_multiple_numbers(self) -> None:

        assert pair(1, 2, 3) == 33
        assert pair(3, 4, 5) == 385
        assert pair(1, 2, 3, 4) == 1126
        assert pair(1, 2, 3, 4, 5) == 1269007

    def test_pair_exceptions(self) -> None:

        with pytest.raises(ValueError):
            assert pair(1)

        with pytest.raises(ValueError):
            assert pair(1, -2)

        with pytest.raises(ValueError):
            assert pair(1,)

        with pytest.raises(ValueError):
            assert pair(1, -2)


class TestSzudzikUnpair(object):

    def test_unpair(self) -> None:

        assert unpair(0) == (0, 0)
        assert unpair(1) == (0, 1)
        assert unpair(2) == (1, 0)
        assert unpair(19) == (3, 4)
        assert unpair(8579) == (92, 23)

        assert unpair(33) == (5, 3)
        assert unpair(33, n=3) == (1, 2, 3)

        assert unpair(385) == (19, 5)
        assert unpair(385, n=3) == (3, 4, 5)

        assert unpair(1126) == (33, 4)
        assert unpair(1126, n=3) == (5, 3, 4)
        assert unpair(1126, n=4) == (1, 2, 3, 4)

    def test_unpair_exceptions(self) -> None:

        with pytest.raises(ValueError):
            assert unpair(0.5)

        with pytest.raises(ValueError):
            assert unpair(-1)


class TestSzudzik(object):

    def test_inverse_property(self) -> None:

        n1, n2 = unpair(pair(1, 2))
        assert n1 == 1 and n2 == 2

        n1, n2 = unpair(33)
        assert pair(n1, n2) == 33
