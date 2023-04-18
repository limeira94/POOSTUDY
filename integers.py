import pytest
from binary import Byte, adder, multiplier, Word, Tribyte, DoubleWord


class Int8:
    def __init__(self, n):
        self.value = Byte(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        if 0 <= sum_ < 256:
            return Int8(sum_)
        else:
            return Int16(sum_)

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        p = multiplier(self.value, other.value)
        if 0 <= p < 256:
            return Int8(p)
        else:
            return Int16(p)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value!r})'


class Int16:
    def __init__(self, n):
        self.value = Word(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        if 0 <= sum_ < 65536:
            return Int16(sum_)
        else:
            return Int24(sum_)

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        p = multiplier(self.value, other.value)
        if 0 <= p < 65536:
            return Int16(p)
        else:
            return Int24(p)


class Int24:
    def __init__(self, n):
        self.value = Tribyte(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        if 0 <= sum_ < 16_777_216:
            return Int24(sum_)
        else:
            return Int32(sum_)

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        p = multiplier(self.value, other.value)
        if 0 <= p < 16_777_216:
            return Int24(p)
        else:
            return Int32(p)


class Int32:
    def __init__(self, n):
        self.value = DoubleWord(n)

    def __add__(self, other):
        sum_ = adder(self.value, other.value)
        return Int32(sum_)

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        return Int32(multiplier(self.value, other.value))



def test_int8():
    assert isinstance(Int8(0), Int8)
    assert isinstance(Int8(255), Int8)
    with pytest.raises(ValueError):
        Int8(256)

    assert Int8(0) + Int8(0) == Int8(0)
    assert Int8(1) + Int8(1) == Int8(2)
    assert Int8(254) + Int8(1) == Int8(255)

    assert Int8(127) * Int8(2) == Int8(254)


def test_int16():
    assert isinstance(Int16(0), Int16)
    assert isinstance(Int16(65535), Int16)
    with pytest.raises(ValueError):
        Int16(65536)

    assert Int16(0) + Int16(0) == Int16(0)
    assert Int16(255) + Int16(1) == Int16(256)

    assert Int16(256) * Int16(2) == Int16(512)


def test_int24():
    assert isinstance(Int24(0), Int24)
    assert isinstance(Int24(16_777_215), Int24)
    with pytest.raises(ValueError):
        Int24(16_777_216)

    assert Int24(0) + Int24(0) == Int24(0)
    assert Int24(65535) + Int24(1) == Int24(65536)

    assert Int24(65536) * Int24(2) == Int24(131_072)


def test_int32():
    assert isinstance(Int32(0), Int32)
    assert isinstance(Int32(4_294_967_295), Int32)
    with pytest.raises(ValueError):
        Int32(4_294_967_296)

    assert Int32(0) + Int32(0) == Int32(0)
    assert Int32(16_777_215) + Int32(1) == Int32(16_777_216)

    assert Int32(16_777_216) * Int32(2) == Int32(33_554_432)


def test_scale_up():
    assert Int8(255) + Int8(1) == Int16(256)
    assert Int8(128) * Int8(2) == Int16(256)

    assert Int16(65535) + Int16(1) == Int24(65536)
    assert Int16(32_768) * Int16(2) == Int24(65536)

    assert Int24(16_777_215) + Int24(1) == Int32(16_777_216)
    assert Int24(8_388_608) * Int24(2) == Int32(16_777_216)
