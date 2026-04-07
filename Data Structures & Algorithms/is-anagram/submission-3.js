class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const s_split = s.split("").sort();
        const t_split = t.split("").sort();
        if (s_split.length !== t_split.length) return false;
        for (let i = 0; i < s_split.length; i++) {
            if (s_split[i] !== t_split[i]) {
                return false;
            }
        }
        return true;
    }
}
