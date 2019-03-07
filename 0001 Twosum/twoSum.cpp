// 解法一：没有引入map
class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		vector<int> res;
		for(int i = 0;i <nums.size(); i++)
		{
			for (int j = 0; j < nums.size(); j++)
			{
				if (i < j && target - nums.at(i) == nums.at(j))
				{
					res.push_back(i);
					res.push_back(j);
				}
			}
		}
		return res;
	}
};

// 解法二：引入 unordered_map
class Solution
{
  public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> v;
        unordered_map<int, int> hash;
        for (int i = nums.size() - 1;i >= 0; hash[nums[i]] = i, i--)
        {
            if (hash.find(target - nums[i]) == hash.end())
                continue;
            v.push_back(i);
            v.push_back(hash[target - nums[i]]);
            return v;
        }
        return v;
    }
};


// 测试
void printVector(vector<int> & v)
{
	for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
	{
		cout << *it << " ";
	}
	cout << endl;
}

int main() 
{
	Solution s;
	vector<int> nums = { 2, 7, 11, 15 };
	int target = 9;
	vector<int> tmp;
	tmp = s.twoSum(nums, target);
	printVector(tmp);
}
















