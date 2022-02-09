def generateParenthesis(n):
    ans = []

    def generate(ll, left, right):
        if len(ll) == 2 * n:
            ans.append(''.join(ll))
            return
        if left < n:
            ll.append('(')
            generate(ll, left + 1, right)
            ll.pop()
        if left > right:
            ll.append(')')
            generate(ll, left, right + 1)
            ll.pop()

    generate([], 0, 0)
    return ans

    # if n == 0:
    #     return ['']
    # res = []
    # for i in range(n):
    #     for left in generateParenthesis(i):
    #         for right in generateParenthesis(n - i - 1):
    #             res.append('({}){}'.format(left, right))
    # return res

print(generateParenthesis(3))
print(generateParenthesis(1))