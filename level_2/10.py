Point = tuple[int, int]


def is_point_in_square(point: Point, left_upper_corner: Point, right_bottom_corner: Point) -> bool:
    x_in_range = left_upper_corner[0] < point[0] < right_bottom_corner[0]
    y_in_range = left_upper_corner[1] < point[1] < right_bottom_corner[1]
    return x_in_range and y_in_range


if __name__ == '__main__':
    assert (  # noqa: S101
        is_point_in_square(point=(10, 12), left_upper_corner=(5, 5), right_bottom_corner=(20, 15)) is True
    )
