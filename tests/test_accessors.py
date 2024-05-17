"""Tests for Herbie xarray accessors.

Note: See `test_pick_points.py` for testing the pick_points accessor.
"""

from herbie import Herbie


def test_crs():
    H = Herbie(
        "2022-12-13 12:00",
        model="hrrr",
        product="sfc",
    )
    ds = H.xarray("TMP:2 m")
    crs = ds.herbie.crs
    assert crs


def test_polygon():
    H = Herbie(
        "2022-12-13 12:00",
        model="hrrr",
        product="sfc",
    )
    ds = H.xarray("TMP:2 m")
    polygons = ds.herbie.polygon
    assert len(polygons) == 2


def test_with_wind():
    ds = Herbie("2024-01-01").xarray("GRD:10 m above").herbie.with_wind()
    assert len(ds) == 4
