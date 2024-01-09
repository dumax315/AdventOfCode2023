with open("day17full.txt", "r") as f:
  grid = [[int(y) for y in x] for x in f.read().split("\n")]
import time
start_time = time.time()


from heapq import heappush, heappop

seen = set()
pq = [(grid[0][1],0,1,0,1,1),(grid[1][0],1,0,1,0,1)]

while pq:
    hl, r, c, dr, dc, n = heappop(pq)

    # print(r,c)

    #   if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])):
    #     continue
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print(hl)
        print("--- %s seconds ---" % (time.time() - start_time))
        break

    if((r, c, dr, dc, n) in seen):
        continue
    
    seen.add((r, c, dr, dc, n))

    if (n < 10) and (dr, dc) != (0,0):
        nr = r + dr
        nc = c + dc
        if( 0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n+1))
    
    for ndr, ndc in [(0,1), (1,0), (0,-1), (-1,0)]:
        if (ndr, ndc) != (dr, dc) and (ndr,ndc) != (-dr, -dc):
            if(n > 3):
                nr = r + ndr
                nc = c + ndc
                if( 0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


