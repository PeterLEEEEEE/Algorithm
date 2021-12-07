def solution(tickets):
    routes = {}
    stack = ["ICN"]
    path = []
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for item in routes:
        routes[item].sort(reverse=True)
    
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    return path[::-1]


if __name__ == '__main__':
    tickets = [["ICN", "SFO"],
               ["ICN", "ATL"],
               ["SFO", "ATL"],
               ["ATL", "ICN"],
               ["ATL", "SFO"]]
    print(solution(tickets))
