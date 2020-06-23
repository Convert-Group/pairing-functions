# -*- coding: utf-8 -*-

import pytest

from pairing_functions.cantor import pair, unpair


class TestCantorPairing(object):

    def test_pair(self) -> None:

        assert pair(0, 0) == 0
        assert pair(0, 1) == 2
        assert pair(1, 0) == 1
        assert pair(2, 2) == 12
        assert pair(3, 4) == 32
        assert pair(47, 32) == 3192
        assert pair(92, 23) == 6693

    def test_pair_multiple_numbers(self) -> None:

        assert pair(1, 2, 3) == 69
        assert pair(3, 4, 5) == 708
        assert pair(1, 2, 3, 4) == 2705
        assert pair(1, 2, 3, 4, 5) == 3673410

    def test_pair_exceptions(self) -> None:

        with pytest.raises(ValueError):
            assert pair(1)

        with pytest.raises(ValueError):
            assert pair(1, -2)

        with pytest.raises(ValueError):
            assert pair(1,)

        with pytest.raises(ValueError):
            assert pair(1, -2)


class TestCantorUnpair(object):

    def test_unpair(self) -> None:

        assert unpair(0) == (0, 0)
        assert unpair(1) == (1, 0)
        assert unpair(2) == (0, 1)
        assert unpair(32) == (3, 4)
        assert unpair(1432) == (52, 1)
        assert unpair(6693) == (92, 23)

        assert unpair(69) == (8, 3)
        assert unpair(69, n=3) == (1, 2, 3)

        assert unpair(708) == (32, 5)
        assert unpair(708, n=3) == (3, 4, 5)

        assert unpair(2705) == (69, 4)
        assert unpair(2705, n=3) == (8, 3, 4)
        assert unpair(2705, n=4) == (1, 2, 3, 4)

    def test_unpair_exceptions(self) -> None:

        with pytest.raises(ValueError):
            assert unpair(0.5)

        with pytest.raises(ValueError):
            assert unpair(-1)


class TestCantor(object):

    def test_inverse_property(self) -> None:

        n1, n2 = unpair(pair(1, 2))
        assert n1 == 1 and n2 == 2

        n1, n2 = unpair(33)
        assert pair(n1, n2) == 33
