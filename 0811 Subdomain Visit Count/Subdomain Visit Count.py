#from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_counts = defaultdict(int)
        for cpdomain in cpdomains:
            times, domains = cpdomain.split(' ')
            times = int(times)
            domain_counts[domains] += times
            while '.' in domains:
                domains = domains[domains.index('.') + 1:]
                domain_counts[domains] += times
        # return [str(v) + ' ' + d for d, v in domain_counts.items()]
        Op = []
        # for d, v in domain_counts.items():
        #     temp = ''
        #     temp += str(v) + ' ' + d
        #     Op.append(temp)
        Op = [str(v) + ' ' + d for d, v in domain_counts.items()]
        return Op