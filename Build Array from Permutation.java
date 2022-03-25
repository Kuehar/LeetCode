class Solution {
    public int[] buildArray(int[] nums) {
        int[] ans = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            ans[i] = nums[nums[i]];
        }
        return ans;
    }
}
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Build Array from Permutation.
// Memory Usage: 42.6 MB, less than 94.17% of Java online submissions for Build Array from Permutation.
