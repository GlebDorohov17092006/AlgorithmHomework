class Solution(object):
    def trap(self, height):
        stack = []
        water, buffer_cub = 0, 0
        for i in range(len(height)):
            if height[i]==0:
                continue
            elif len(stack)==0:
                stack.append([height[i], i])
            elif stack[-1][0] > height[i]:
                stack.append([height[i], i])
            else:
                last_elem = 0
                while stack and stack[-1][0] <= height[i]:
                    if len(stack)>1:
                        buffer_cub += stack[-1][0]
                    last_elem = stack[-1]
                    stack.pop()
                if not(stack):
                    water += last_elem[0] * (i - last_elem[1] - 1) - buffer_cub
                    buffer_cub = 0
                stack.append([height[i], i])
        if not(stack):
            return water - buffer_cub
        prev = stack[-1]
        stack.pop()
        while stack:
            water += prev[0] * ( prev[1] - stack[-1][1] - 1 )
            prev = stack[-1]
            stack.pop()

        return water - buffer_cub