** start of main.py **

def hanoi_solver(n):
    a=[a for a in range(n,0,-1)]
    b=[]
    c=[]
    lines=[a,b,c]
    #initialisation of the return string "moves"
    moves=f"{lines[0]} {lines[1]} {lines[2]}"
#choose target column
#example 3

    #for easier recursion the columns a,b and c has been assigned to a list, we are dealing with their call using their indexes
    def recursive_move(n,start,end):
        nonlocal moves
        if n==0:
            return
        #give a reference to the third pole
        other=3-(start+end)

        recursive_move(n-1,start,other)
        #move the disk from the starting position to the end position
        disk = lines[start].pop()
        lines[end].append(disk)
        moves+=f"\n{lines[0]} {lines[1]} {lines[2]}"
        
        recursive_move(n-1,other,end)

    recursive_move(n,0,2)
    #print(moves)
    return moves



if __name__=="__main__":
    hanoi_solver(12)

** end of main.py **

