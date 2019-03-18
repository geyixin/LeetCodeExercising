/*
二进制数相加，并且保存在string中。

3点注意：

1. 如何将string数字和int数字之间互相转换：a[i]-'0'；
2. 并且每位相加时，会有进位的可能，会影响之后相加的结果：引入进位标志符move；
3. 两个输入string的长度也可能会不同：较短的用'0'补齐；
*/

// 方法一

class Solution {
public:
	string addBinary(string a, string b) {
		int len_a = a.size();
		int len_b = b.size();
		int len_max = max(len_a, len_b);
		bool move = false;
		string res;
		if (len_a < len_b)
			for (int i = 0;i < len_b - len_a;i++)
				a.insert(a.begin(),'0');
		if (len_a > len_b)
			for (int j = 0; j < len_a - len_b;j++)
				b.insert(b.begin(), '0');

		for (int k = len_max-1; k >= 0;k--)
		{
			int tmp = 0;
			if (move)
				tmp = (a[k] - '0') + (b[k] - '0') + 1;
			else
				tmp = (a[k] - '0') + (b[k] - '0');
			if (tmp == 0)
			{
				res.insert(res.begin(), '0');
				move = false;
			}
			else if(tmp==1)
			{
				res.insert(res.begin(), '1');
				move = false;
			}
			else if (tmp == 2)
			{
				res.insert(res.begin(), '0');
				move = true;
			}
			else if (tmp == 3)
			{
				res.insert(res.begin(), '1');
				move = true;
			}
		}
		if (move)
			res.insert(res.begin(), '1');
		return res;
	}
};



// 方法二

/*
用了两个指针分别指向a和b的末尾，然后每次取出一个字符，转为数字，若无法取出字符则按0处理，然后定义进位carry，初始化为0，将三者加起来，对2取余即为当前位的数字，对2取商即为当前进位的值，记得最后还要判断下carry，如果为1的话，要在结果最前面加上一个。
*/

class Solution {
public:
	string addBinary(string a, string b) {
		string res = "";
		int len_a = a.size() - 1;
		int len_b = b.size() - 1;
		int move = 0;
		while (len_a >=0 || len_b>=0)
		{
			int m = len_a >= 0 ? a[len_a--] - '0' : 0;
			int n = len_b >= 0 ? b[len_b--] - '0' : 0;
			int sum = m + n + move;
			res = to_string(sum % 2) + res;
			move = sum / 2;
		}
		return move== 1 ? '1' + res : res;
	}
};



