# -*- coding: utf-8 -*-
"""
Project Euler Problem 59

http://projecteuler.net/index.php?section=problems&id=59

Each character on a computer is assigned a unique code and the
preferred standard is ASCII (American Standard Code for Information
Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes
to ASCII, then XOR each byte with a given value, taken from a secret
key. The advantage with the XOR function is that using the same
encryption key on the cipher text, restores the plain text; for
example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain
text message, and the key is made up of random bytes. The user would
keep the encrypted message and the encryption key in different
locations, and without both "halves", it is impossible to decrypt the
message.

Unfortunately, this method is impractical for most users, so the
modified method is to use a password as a key. If the password is
shorter than the message, which is likely, the key is repeated
cyclically throughout the message. The balance for this method is
using a sufficiently long password key for security, but short enough
to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt , a file containing the
encrypted ASCII codes, and the knowledge that the plain text must
contain common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""
import string
from itertools import product, cycle
from operator import xor

def read_cipher():
    """
    Reads the cipher from cipher1.txt and returns a list of integers.
    """
    f = open('cipher1.txt')
    cipher = f.read().strip()
    # conver
    return [int(x) for x in cipher.split(",")]

class Message(object):
    def __init__(self, cipher, key):
        """
        Initialise message.

        cipher - the cipher as a list of integers
        key - the key as a string
        """
        self.key = [ord(k) for k in key]
        self.cipher = cipher

    def decrypt(self):
        """
        Decrypts the cipher with the key, and caches the list of
        original ASCII values in self._ascii_values.

        Returns None
        """
        repeated_key = cycle(self.key)
        ascii_values = []
        for c, k in zip(self.cipher, repeated_key):
            ascii_values.append(xor(c, k))
        self._ascii_values = ascii_values

    @property
    def ascii_values(self):
        if not hasattr(self, '_ascii_values'):
            self.decrypt()
        return self._ascii_values
                          

    @property
    def as_string(self):
        """
        Return the message as a string
        """
        if not hasattr(self, '_ascii_values'):
            self.decrypt()
        return "".join(chr(b) for b in self._ascii_values)

    def is_decrypted(self, words=()):
        """
        Runs heuristic to predict whether we are using the correct key.

        1. Returns false if there are any control characters
        2. Returns false if any of the words in words does not appear
           in the message. The words are padded with space so for example
           "there" will not match "the".
        """
        if not hasattr(self, 'ascii_values'):
            self.decrypt()
        for b in self.ascii_values:
            if 0 <= b <= 31:
                return False

        if words:
            padded_words = [" %s " % word for word in words]
        for word in padded_words:
            if word not in self.as_string:
                return False
        return True

def solution():
    """
    Try to decrypt the cipher using all keys which consist of three
    lowercase ASCII characters.

    When a solution is found, return the sum of the ASCII values in
    decrypted message.
    """
    # Words have been chosen after the problem has been solved
    # so that is_decrypted only returns True for the solution.
    WORDS = ["and", "the"]

    cipher = read_cipher()
    for key in product(string.ascii_lowercase, string.ascii_lowercase, string.ascii_lowercase):
        message = Message(cipher, key)
        if message.is_decrypted(words=WORDS):
            # print message.as_string
            return sum(message.ascii_values)

if __name__ == "__main__":
    print solution()
