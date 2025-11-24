                        #       *      *
                        #       **    **
                        #       * *  * *
                        #       *  **  *
                        #       *  **  *
                        #       * *  * *
                        #       **    **
                        #       *      *

n = 8
for i in range(n):
    # if i == 1 or i == n-1:
    #     print("*" + " "*(n-2) + "*")
    for j in range(i-1):
        print("*"+ " "*j + "*" )
        
        
