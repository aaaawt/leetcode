def groupAnagrams(strs):
    dd = {}
    for s in strs:
        k = ''.join(sorted(s))
        if k not in dd:
            dd[k] = [s]
        else:
            dd[k].append(s)
    return list(dd.values())

print(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print(groupAnagrams(['']))
print(groupAnagrams(['a']))
