def search (arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = ["నమస్తే", "తెలుగు", "భాష", "స్వాగతం", "కోడ్"]
x = "స్వాగతం"
N = len(arr)
result = search(arr, x)
if result == -1:
    print("Element is not present in array")
else:
    print(f"Element is present at index {result}")