""" 2062. 统计字符串中的元音子字符串（266周赛，1）
子字符串 是字符串中的一个连续（非空）的字符序列。

元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。

给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。

示例 1：
输入：word = "aeiouu"
输出：2
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "aeiou"
- "aeiouu"

示例 2：
输入：word = "unicornarihan"
输出：0
解释：word 中不含 5 种元音，所以也不会存在元音子字符串。

示例 3：
输入：word = "cuaieuouac"
输出：7
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "uaieuo"
- "uaieuou"
- "uaieuoua"
- "aieuo"
- "aieuou"
- "aieuoua"
- "ieuoua"

示例 4：
输入：word = "bbaeixoubb"
输出：0
解释：所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。

提示：
    1 <= word.length <= 100
    word 仅由小写英文字母组成
"""


def count_vowel_substrings(word):
    vowel, cnt, n = set("aeiou"), 0, len(word)
    for i in range(n-1):
        for j in range(i, n+1):
            cnt += 1 if set(word[i:j]) == vowel else 0
    return cnt


def count_vowel_substrings2(word):
    vowel, cnt, n = set("aeiou"), 0, len(word)
    for i in range(n-1):
        char_set = set()
        for j in range(i, n):
            char_set.add(word[j])
            cnt += 1 if char_set == vowel else 0
    return cnt
