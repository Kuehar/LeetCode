class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        fixed_email = set()
        for lists in emails:
            local,domain = lists.split("@")
            local = local.split("+")[0].replace(".","")
            fixed_email.add(local + "@" + domain)
        return len(fixed_email)
# Runtime: 52 ms, faster than 77.31% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 14.2 MB, less than 5.16% of Python3 online submissions for Unique Email Addresses.
