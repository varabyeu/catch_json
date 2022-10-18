def relations(network: tuple) -> dict:
    relations_from_top = {}
    for relation in network:
        if not relations_from_top.get(relation[0]):
            relations_from_top[relation[0]] = [relation[1], ]
        else:
            values_first = relations_from_top[relation[0]]
            values_first.append(relation[1])
        if not relations_from_top.get(relation[1]):
            relations_from_top[relation[1]] = [relation[0], ]
        else:
            values_second = relations_from_top[relation[1]]
            values_second.append(relation[0])
    return relations_from_top


def check_relation(net, first, second, depth=0, related=None):
    if related is None:
        related = relations(net)
    person_network = related[first]
    if second in person_network:
        return True
    else:
        for person in person_network:
            depth += 1
            if depth > len(related):
                return False
            first, second = second, person
            return check_relation(net, first, second, depth, related)


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
