class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arrLength = len(nums)
        # define post and pre products
        preProd = [1] * arrLength
        postProd = [1] * arrLength

        preSum = 1
        postSum = 1
        for i in range(1, arrLength):
            # update the product of numbers before the current
            preSum *= nums[i-1]
            preProd[i] = preSum

        for j in range(arrLength - 2, -1, -1):
            # update the product of numbers after j
            postSum *= nums[j + 1]
            postProd[j] = postSum

        output = []
        for pos in range(arrLength):
            product = preProd[pos] * postProd[pos]
            output.append(product)

        return output


        