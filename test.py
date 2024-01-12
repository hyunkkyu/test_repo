def do_multiplication_tb2():
    for i in range(1, 10):
        print(f"{i}단: ", end="")
    for j in range(1, 10):
        print(f"{i*j}", end=" ")
    print()  # Removed extra newline for cleaner output

if __name__=='__main__':
 do_multiplication_tb2()
