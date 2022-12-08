
def find_pairs(items: list, voucher: int) -> set:
    result = set()
    prices = dict()

    for item in items:
        if item[1] not in prices:
            prices[item[1]] = []
        prices[item[1]].append(item)

    
    check = list()
    for key in prices:
        for el in prices[key]:
            check.append(key)
            
    values_pairs = pairs_values(check, voucher)
    for pair in values_pairs:
        for first_el in prices[pair[0]]:
            for sec_el in prices[pair[1]]:
                item = (first_el, sec_el)
                if item not in result and (sec_el, first_el) not in result:
                    result.add(item)

    return result   

    
    
def pairs_values(items: list, voucher: int) -> set:
    result = set()
    items.sort()
    start = 0
    end = len(items) - 1

    while start < end:
        if (items[start] + items[end]) == voucher:
            result.add((items[start], items[end]))
            start += 1
            end -= 1
            continue

        if (items[start] + items[end]) > voucher:
            end -= 1
            continue

        if (items[start] + items[end]) < voucher:
            start += 1
            continue
    

    return result
