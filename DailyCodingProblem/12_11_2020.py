'''This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''
from itertools import permutations

def get_mapping():
    map = dict()

    for indx,char in enumerate(range(ord('a'), ord('z')+1),1):
        map[indx] = chr(char)

    return map


def decode_msg(encoded_msg):
    return ''.join([map_[i] for i in list(map(int, str(encoded_msg)))])

if __name__ == '__main__':
    map_ = get_mapping()

    encoded_msg = int(input('Enter message to decode.....'))
    decoded_msg = decode_msg(encoded_msg)

    msg_permutations = []
    for i in range(2, len(decoded_msg)+1):
        msg_permutations.extend(list(permutations(decoded_msg, i)))

    print(len(msg_permutations))
