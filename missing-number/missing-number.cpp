class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int x=nums[0];
        vector<int> arr;
        for(int i=0; i<=nums.size(); i++)
        {
            arr.push_back(i);
        }
        for(int i=1; i<nums.size();i++)
        {
            x^=nums[i];
        }
        for(int i=0; i<arr.size();i++)
        {
            x^=arr[i];
        }
        return x;
    }
};