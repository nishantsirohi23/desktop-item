import heapq
def shortest_time_to_reach_expert(N, member_ids, edges, follower, following):
    graph = create_weighted_graph(N, edges,member_ids)  # Create a weighted graph representation


    distances = {member_id:float('inf') for member_id in member_ids}
    distances[follower]= 0
    q = [(0,follower)]
    while q:
        time,current = heapq.heappop(q)
        if current == following:
            return time

        for next,m_time in graph[current]:
            new_time = time + m_time
            if new_time<distances[next]:
                distances[next] = new_time
                heapq.heappush(q,(new_time,next))

    return -1
