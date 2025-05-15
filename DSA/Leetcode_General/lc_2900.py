

def getLongestSubsequence(words, groups):

        output = [words[0]]
        prev_bit = groups[0]

        # for i in range(1,len(words)):
        #     if prev_bit == 0 and groups[i] == 1:
        #         output.append(words[i])
        #         prev_bit = 1
        #     elif prev_bit == 1 and groups[i] == 0:
        #         output.append(words[i])
        #         prev_bit = 0

        # return output


        for i in range(1,len(words)):
            if groups[i] == prev_bit:
                    continue
            
            output.append(words[i])
            # prev_bit = not(prev_bit)
            prev_bit = int(not(prev_bit)) # both true

        return output
        






words1 = ["e","a","b"]
groups1 = [0,0,1]
words2 = ["a","b","c","d"]
groups2 = [1,0,1,1]


print(getLongestSubsequence(words1,groups1))
print(getLongestSubsequence(words2,groups2))