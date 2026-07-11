class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
        max_freq = max(frequencies)
        max_freq_count = frequencies.count(max_freq)
        ans = (max_freq - 1) * (n + 1) + max_freq_count
        return max(ans,len(tasks))

        