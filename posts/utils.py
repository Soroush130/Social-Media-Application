def group_list(li: list, count_group: int) -> list:
    return [li[n:n + count_group] for n in range(0, len(li), count_group)]
