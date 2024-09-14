class Solution(object):
    def stableMountains(self, height, threshold):
        l = len(height)
        f = []
        for i in range(1,l):
            if height[i-1]>threshold:
                f.append(i)
        return f





        