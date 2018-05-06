'''
由于颜色肯定是正数 1 到 k，所以我们可以用负数比如 colors [i] = -k，表示第 i 种颜色在原来的数组里面出现了 k 次。
首先f遍历一遍原来的数组，如果扫到 colors[i]，首先检查 colors[colors[i]] 是否为正数，如果是把 colors[colors[i]] 移动colors[i] 存放起来，然后把 colors[colors[i]] 记为-1(表示该位置是一个计数器，计1)。 如果 colors[colors[i]] 是负数，那么说明这一个地方曾经已经计数了，那么把 colors[colors[i]] 计数减一，并把color[i] 设置为0 （表示此处已经计算过），然后重复向下遍历下一个数，这样遍历原数组所有的元素过后，数组 colors[i] 里面实际上存储的每种颜色的计数，然后我们倒着再输出每种颜色就可以得到我们排序后的数组。
'''

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        if colors is None or len(colors) == 0:
            return colors
        idx, l = 0, len(colors)
        while idx < l:
            tmp = colors[idx] - 1
            if colors[idx] <= 0:
                idx += 1
            else:
                if colors[tmp] <= 0:
                    colors[tmp] -= 1
                    colors[idx] = 0
                    idx += 1
                else:
                    colors[idx], colors[tmp] = colors[tmp], colors[idx]
                    colors[tmp] = -1
        i = l - 1
        while k > 0:
            for j in xrange(0, colors[k-1], -1):
                colors[i] = k
                i -= 1
            k -= 1