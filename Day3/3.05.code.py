def minJump(nums):
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps
arr=[1,3,5,8,9,2,6,7,6,8,9]
print("arr[]=",arr)
print(minJump(arr))
arr1=[1,1,1,1,1,1,1,1,1,1]
print("arr1[]=",arr1)
print(minJump(arr1))
arr2=[2,3,1,1,4]
print("arr2[]=",arr2)
print(minJump(arr2))
arr3=[1,3,6,1,0,9]
print("arr3[]=",arr3)
print(minJump(arr3))
arr4=[2,3,0,1,4]
print("arr4[]=",arr4)
print(minJump(arr4))
