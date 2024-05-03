

# Input-Restricted Queue(Only one input operation->(push) )
# 1. Push_back(rear)
# 2. Pop_front()
# 3. Pop_back(rear)


input_restricted = [1,2,3,5,56,36,6]
input_restricted.append(35) # push_back
input_restricted.pop() # pop_back
input_restricted.pop(0) # pop_front


# Output-Restricted Queue(Only one output operation->(pop))
# 1. Push_back(rear)
# 2. Push_front(front)
# 3. Pop_back(rear)

output_restricted = [1,2,3,5,56,36,6]
output_restricted.append(53) # push_back
output_restricted.insert(0,253) # push_front
output_restricted.pop() # pop_back