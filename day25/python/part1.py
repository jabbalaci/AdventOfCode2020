#!/usr/bin/env python3

import helper


class Crypto:
    def __init__(self, card_public_key: int, door_public_key: int) -> None:
        self.card_public_key = card_public_key
        self.door_public_key = door_public_key
        self.subject_number = 7
        self.magic_number = 20201227
        self.card_loop_size = -1
        self.door_loop_size = -1
        self.encryption_key = -1

    def find_card_loop_size(self) -> int:
        value = 1
        cnt = 0
        while True:
            cnt += 1
            value *= self.subject_number
            value = value % self.magic_number
            if value == self.card_public_key:
                break
            #
        #
        return cnt

    def find_door_loop_size(self) -> int:
        value = 1
        cnt = 0
        while True:
            cnt += 1
            value *= self.subject_number
            value = value % self.magic_number
            if value == self.door_public_key:
                break
            #
        #
        return cnt

    def find_encryption_key(self) -> int:
        value = 1
        #
        if self.card_loop_size < self.door_loop_size:
            for _ in range(self.card_loop_size):
                value *= self.door_public_key
                value = value % self.magic_number
            #
        else:
            for _ in range(self.door_loop_size):
                value *= self.card_public_key
                value = value % self.magic_number
        #
        return value

    def start(self) -> None:
        print("card's public key:", self.card_public_key)
        print("door's public key:", self.door_public_key)
        self.card_loop_size = self.find_card_loop_size()
        print("card's loop size:", self.card_loop_size)
        self.door_loop_size = self.find_door_loop_size()
        print("door's loop size:", self.door_loop_size)
        self.encryption_key = self.find_encryption_key()


def main() -> None:
    # card_public_key, door_public_key = helper.read_lines_as_ints("example.txt")
    card_public_key, door_public_key = helper.read_lines_as_ints("input.txt")

    # print(card_public_key)
    # print(door_public_key)

    crypto = Crypto(card_public_key, door_public_key)
    crypto.start()
    print()
    print("encryption key:", crypto.encryption_key)

##############################################################################

if __name__ == "__main__":
    main()
