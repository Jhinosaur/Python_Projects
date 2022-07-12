answers = []

def bigger_is_greater(word):
    arr = list(word)

    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return 'no answer'

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return "".join(arr)


if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = bigger_is_greater(w)
        answers.append(result)

for word in answers:
    print(word)