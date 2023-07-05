n = int(input())
arr = map(int, input().split())

a = list(arr)

if 2 <= n <= 10:
    if len(a) == n:
        if all(-100 <= num <= 100 for num in a):
            unique_scores = list(set(a))  # Remove duplicates and convert to list
            if len(unique_scores) > 1:
                unique_scores.remove(max(unique_scores))
                runner_up_score = max(unique_scores)
                print(runner_up_score)
            else:
                print("No runner-up score")