import sys
input = sys.stdin.read

def main():
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    numbers = list(map(int, data[2:n+2]))
    
    prefix_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]
    
    result = []
    
    index = n + 2
    for _ in range(m):
        i = int(data[index])
        j = int(data[index + 1])
        index += 2
        result.append(str(prefix_sum[j] - prefix_sum[i - 1]))
    
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()