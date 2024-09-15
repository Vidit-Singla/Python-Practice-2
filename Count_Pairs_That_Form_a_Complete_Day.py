class Solution(object):
    def countCompleteDayPairs(self, hours):
        f = []
       
        for i in range(len(hours)):
            for j in range(len(hours)):       
                if (hours[i] + hours[j]) % 24 == 0:
                    f.append((i, j))

 
        def cleaner(pair):
            return pair[0] == pair[1] or pair[0] > pair[1]

        
        f_filtered = [pair for pair in f if not cleaner(pair)]
        
        return len(f_filtered)
