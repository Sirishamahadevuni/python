def largestRectangleArea(heights):
    # Add a 0 height at the end to handle the remaining bars in the stack
    heights.append(0)
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        # If the stack is empty or the current height is greater than the height at the top of the stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top of the stack and calculate the area with the popped height
            height = heights[stack.pop()]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)

    return max_area

# Input
n = int(input())
heights = list(map(int, input().split()))

# Output
print(largestRectangleArea(heights))
