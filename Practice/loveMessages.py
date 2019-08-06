from collections import defaultdict
from typing import List
from heapq import heappush, heappop

class LoveMessage:
    def topLovesReceiver(self, love_msgs: List[dict]):
        love_Dict = defaultdict(list)
        max_loves = 0
        max_receiver = None

        for msg in love_msgs:
            love_Dict[msg["receiver"]].append((msg["sender"], msg["msg"]))

        for receiver, msg_list in love_Dict.items():
            if len(msg_list) > max_loves:
                max_loves = len(msg_list)
                max_receiver = receiver
                
        return max_receiver

    def topKLovesReceiver(self, love_msgs: List[dict], k: int):
        love_Dict = defaultdict(list)
        heap = []
        for msg in love_msgs:
            love_Dict[msg["receiver"]].append((msg["sender"], msg["msg"]))

        for receiver, msg_list in love_Dict.items():
            numOfLoves = len(msg_list)
            heappush(heap, (numOfLoves, receiver))
            if len(heap) > k:
                heappop(heap)

        return [n[1] for n in heap[::-1]]


love_msgs = [
    {
        "sender": "david@yelp.com",
        "receiver": "ryan@yelp.com",
        "msg": "Hello World"
    },
    {
        "sender": "nina@yelp.com",
        "receiver": "ryan@yelp.com",
        "msg": "H"
    },
    {
        "sender": "bran@yelp.com",
        "receiver": "nina@yelp.com",
        "msg": "Could you forward the email ryan sent you?"
    },
    {
        "sender": "cv_json@yelp.com",
        "receiver": "david@yelp.com",
        "msg": "Check out this awesome website"
    },
    {
        "sender": "andy@yelp.com",
        "receiver": "nina@yelp.com",
        "msg": "Meet me in 5 min"
    },
    {
        "sender": "jason@yelp.com",
        "receiver": "nina@yelp.com",
        "msg": "Wanna have dinner tonight?"
    },

]

print(LoveMessage().topKLovesReceiver(love_msgs, 2))