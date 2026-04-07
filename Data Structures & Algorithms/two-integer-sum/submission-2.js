class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numsCopy = nums.map((v, i) => [v, i]);
        const numsCopySorted = numsCopy.sort((a, b) => a[0] - b[0]);
        let leftPtr = 0;
        let rightPtr = nums.length - 1;
        let total = numsCopySorted[leftPtr][0] + numsCopySorted[rightPtr][0];
        while (total !== target) {
            total =
            total < target
                ? numsCopySorted[++leftPtr][0] + numsCopySorted[rightPtr][0]
                : numsCopySorted[leftPtr][0] + numsCopySorted[--rightPtr][0];
        }
        return [numsCopySorted[leftPtr][1], numsCopySorted[rightPtr][1]].sort(
            (a, b) => a - b
        );
    }
}
