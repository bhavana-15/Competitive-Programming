# Next Greater Node In Linked List

**Hint**
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

### Example 1:

[linkedlistnext1](https://github.com/bhavana-15/Competitive-Programming/assets/157963061/b49b81dd-0455-420c-992d-015461d75cc0)
```
Input: head = [2,1,5]
Output: [5,5,0]
```
### Example 2:
![linkedlistnext2](https://github.com/bhavana-15/Competitive-Programming/assets/157963061/254588ac-03bf-446d-ac99-5f4f2082c3b7)

```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
 
```
**Constraints:**

The number of nodes in the list is n.
1 <= n <= 104
1 <= Node.val <= 109
