TEST_EXAMPLE = {
    "ka": {"de", "ta", "tb", "co"},
    "co": {"de", "ta", "tc", "ka"},
    "ta": {"de", "kh", "ka", "co"},
    "de": {"ka", "ta", "cg", "co"},
    "kh": {"ta", "ub", "qp", "tc"},
    "tc": {"td", "kh", "wh", "co"},
    "qp": {"wh", "td", "kh", "ub"},
    "cg": {"de", "aq", "yn", "tb"},
    "yn": {"wh", "td", "aq", "cg"},
    "aq": {"wq", "cg", "yn", "vc"},
    "ub": {"wq", "kh", "qp", "vc"},
    "tb": {"ka", "wq", "cg", "vc"},
    "vc": {"wq", "aq", "ub", "tb"},
    "wh": {"yn", "td", "qp", "tc"},
    "td": {"yn", "wh", "qp", "tc"},
    "wq": {"aq", "ub", "tb", "vc"},
}
trimmed = {
    "ka": {"ta", "de", "tb", "co"},
    "co": {"tc", "ta", "de"},
    "ta": {"kh", "de"},
    "de": {"cg"},
    "kh": {"tc", "qp", "ub"},
    "tc": {"td", "wh"},
    "qp": {"td", "wh", "ub"},
    "cg": {"yn", "tb", "aq"},
    "yn": {"td", "wh", "aq"},
    "aq": {"vc", "wq"},
    "ub": {"vc", "wq"},
    "tb": {"vc", "wq"},
    "vc": {"wq"},
    "wh": {"td"},
    "td": set(),
    "wq": set(),
}


def crack_password_fail_for_real_input(connections):
    for key, connected in connections.items():
        for conn in connected:
            connections[conn].remove(key)
    largest_group_size = 0
    largest_group = {}
    for key, values in connections.items():
        values_list = list(values)
        group = {key}
        for i, val in enumerate(values_list):
            for other in values_list[:i] + values_list[i + 1 :]:
                if other in connections[val] or val in connections[other]:
                    group.add(other)
                    group.add(val)

        if len(group) > largest_group_size:
            largest_group_size = len(group)
            largest_group = group

    lg = sorted(list(largest_group))
    return ",".join(lg)


def test_find_most_connected():
    assert crack_password_fail_for_real_input(TEST_EXAMPLE) == "co,de,ka,ta"
