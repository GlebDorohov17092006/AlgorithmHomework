class Solution:
    def largestRectangleArea(self, height):
        stack = []
        answer = 0
        height += [0]
        for i in range(len(height)):
            while stack and height[i] <= height[stack[-1]]:
                h, w = height[stack.pop()], i
                if stack:
                    w = i - stack[-1] - 1
                answer = max(answer, h*w)
            stack.append(i)
        return answer