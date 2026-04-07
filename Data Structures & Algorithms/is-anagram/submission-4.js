class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        const ssort = s.split("").sort().join();
        const tsort = t.split("").sort().join();
        return ssort === tsort
    }
}
