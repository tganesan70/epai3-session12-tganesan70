##########################################################################
# pytest script for Session12 assignment
#
# Ganesan Thiagarajan, 25th July 2021
##########################################################################
#
from Polygon import *
from Polygon_lazy import *
import pytest
import inspect
import os
import re
from math import isclose

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# test cases for Polygon objects

abs_tol = 0.001
rel_tol = 0.001


def test_polygon1():
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass

def test_polygon2():
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                ' expected: 60')

def test_polygon3():
    n = 4
    R = 1
    p = Polygon(n, R)
    if p.count_vertices == n:
        assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
        assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

        assert math.isclose(p.side_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.side_length},'
                                           f' expected: {math.sqrt(2)}')

        assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

        assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
def test_polygon4():
    p = Polygon(6, 2)
    if p.count_edges == 6:
        assert math.isclose(p.side_length, 2,
                            rel_tol=rel_tol, abs_tol=abs_tol)
        assert math.isclose(p.apothem, 1.73205,
                            rel_tol=rel_tol, abs_tol=abs_tol)
        assert math.isclose(p.area, 10.3923,
                            rel_tol=rel_tol, abs_tol=abs_tol)
        assert math.isclose(p.perimeter, 12,
                            rel_tol=rel_tol, abs_tol=abs_tol)
        assert math.isclose(p.interior_angle, 120,
                            rel_tol=rel_tol, abs_tol=abs_tol)

def test_polygon5():
    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    #assert math.isclose(p.max_efficiency , p.area / p.perimeter,
    #                    rel_tol = rel_tol, abs_tol = abs_tol)

def test_polygon6():
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

def test_polygon_lazy1():
    try:
        p = PolygonLazy(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass

def test_polygon_lazy2():
    n = 3
    R = 1
    mypoly = PolygonLazy(n, R)
    assert str(mypoly) == 'Polygon(n=3, R=1)', f'actual: {str(mypoly)}'
    for p in mypoly:
        assert p.count_vertices() == n, (f'actual: {p.count_vertices()},'
                                         f' expected: {n}')
        assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
        assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
        assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                        ' expected: 60')

def test_polygon_lazy3():
    n = 4
    R = 1
    mypoly = PolygonLazy(n, R)
    for p in mypoly:
        if p.count_vertices == n:
            assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                            ' expected: 90')
            assert math.isclose(p.area, 2,
                                rel_tol=abs_tol,
                                abs_tol=abs_tol), (f'actual: {p.area},'
                                                   ' expected: 2.0')

            assert math.isclose(p.side_length, math.sqrt(2),
                                rel_tol=rel_tol,
                                abs_tol=abs_tol), (f'actual: {p.side_length},'
                                                   f' expected: {math.sqrt(2)}')

            assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                                rel_tol=rel_tol,
                                abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                                   f' expected: {4 * math.sqrt(2)}')

            assert math.isclose(p.apothem, 0.707,
                                rel_tol=rel_tol,
                                abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                                   ' expected: 0.707')
def test_polygon_lazy4():
    poly = PolygonLazy(6, 2)
    for p in poly:
        if p.count_edges == 6:
            assert math.isclose(p.side_length, 2,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.apothem, 1.73205,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.area, 10.3923,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.perimeter, 12,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.interior_angle, 120,
                                rel_tol=rel_tol, abs_tol=abs_tol)

def test_polygon_lazy5():
    mypoly = PolygonLazy(12, 3)
    for p in mypoly:
        if p.count_edges == 12:
            assert math.isclose(p.side_length, 1.55291,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.apothem, 2.89778,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.area, 27,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.perimeter, 18.635,
                                rel_tol=rel_tol, abs_tol=abs_tol)
            assert math.isclose(p.interior_angle, 150,
                                rel_tol=rel_tol, abs_tol=abs_tol)

def test_polygon6():
    p1 = PolygonLazy.PolygonIter._polygon(3, 10)
    p2 = PolygonLazy.PolygonIter._polygon(10, 10)
    p3 = PolygonLazy.PolygonIter._polygon(15, 10)
    p4 = PolygonLazy.PolygonIter._polygon(15, 100)
    p5 = PolygonLazy.PolygonIter._polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

def test_polygons_next():
    my_polygons = PolygonLazy.PolygonIter(10,2)
    assert my_polygons.__len__() == 8, "Polygon numbers not initialized correctly"
    my_polygons.__next__()
    my_polygons.__next__()
    my_polygons.__next__()
    my_polygons.__next__()
    my_polygons.__next__()
    assert my_polygons._init_poly == 8, "Next iteration not working correctly"

def test_func_doc_strings():
    # Get all functions from PolygonSeq
    func_list = [o for o in inspect.getmembers(Polygon) if inspect.isfunction(o[1])]
    for fn in [f[0] for f in func_list]:
        assert check_doc_string(
            getattr(Polygon, fn)) == True, "Not enough details in the docstring for function " + fn

def test_MyPolygon1():
    try:
        p = MyPolygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass

def test_MyPolygon3():
    n = 4
    R = 1
    p = MyPolygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

    assert math.isclose(p.side_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.side_length},'
                                           f' expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
def test_MyPolygon4():
    p = MyPolygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

def test_MyPolygon5():
    p = MyPolygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)

def test_MyPolygon6():
    p1 = MyPolygon(3, 10)
    p2 = MyPolygon(10, 10)
    p3 = MyPolygon(15, 10)
    p4 = MyPolygon(15, 100)
    p5 = MyPolygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

# End of test_session12
