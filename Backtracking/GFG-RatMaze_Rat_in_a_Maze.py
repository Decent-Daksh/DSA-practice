class Solver:
    def rat_in_the_maze(self,maze:list[list[int]])-> list[str]:
        moves =[(1,0,'D'),(0,-1,'L'),(0,1,'R'),(-1,0,'U')]
        path =[]
        result =[]
        N = len(maze)
        if maze[0][0]==0:
            return []
        maze[0][0] =0
        def solver(row, col):
            if row==N-1 and col == N-1:
                result.append(''.join(path))
                return
            for r,c,d in moves:
                nr= row+r
                nc = col+c
                if  not 0<=nr<N or not 0<=nc<N:
                    continue
                if maze[nr][nc]== 1:
                    maze[nr][nc]=0
                    path.append(d)
                    solver(nr,nc)
                    maze[nr][nc]=1
                    path.pop()
            return
        solver(0,0)
        return result


