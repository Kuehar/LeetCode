class Logger:

    def __init__(self):
        self.msg_hash = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # 存在しない場合
        if message not in self.msg_hash:
            self.msg_hash[message] = timestamp
            return True
        
        
        # 存在するが、10秒以上経過している場合
        if timestamp - self.msg_hash[message]  > 9:
            self.msg_hash[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# Runtime: 144 ms, faster than 75.78% of Python3 online submissions for Logger Rate Limiter.
# Memory Usage: 19.8 MB, less than 82.93% of Python3 online submissions for Logger Rate Limiter.
