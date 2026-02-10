
from ndfl import calculate_tax

def test_basic_ndfl():
  assert calculate_tax(200_000) == 26_000


def test_ndfl_tier_2():
    # 312 000 + 0.15 * 600_000
    assert calculate_tax(3_000_000) == 402_000

def test_ndfl_tier_3():
    # 702_000 + 0.18 * 2_000_000
    assert calculate_tax(7_000_000) == 1_062_000

def test_ndfl_tier_4():
    # 3_402_000 + 0.20 * 10_000_000
    assert calculate_tax(30_000_000) == 5_402_000

def test_ndfl_tier_5():
    # 9_402_000 + 0.22 * 20_000_000
    assert calculate_tax(70_000_000) == 13_802_000
    