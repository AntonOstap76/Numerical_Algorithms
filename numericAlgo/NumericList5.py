#2
# def are_anagrams(phrase1, phrase2):
#
#     phrase1 = phrase1.replace(" ", "").lower()
#     phrase2 = phrase2.replace(" ", "").lower()
#
#
#     if len(phrase1) != len(phrase2):
#         return False
#
#     letter_count1 = {}
#     letter_count2 = {}
#     for char in phrase1:
#         letter_count1[char] = letter_count1.get(char, 0) + 1
#     for char in phrase2:
#         letter_count2[char] = letter_count2.get(char, 0) + 1
#
#     # Compare the letter counts
#     return letter_count1 == letter_count2
#
#
# # Test the function
# phrase1 = "listen"
# phrase2 = "silent"
# if are_anagrams(phrase1, phrase2):
#     print(f"{phrase1} and {phrase2} are anagrams.")
# else:
#     print(f"{phrase1} and {phrase2} are not anagrams.")


#3
# def is_palindrom(word1):
#     new_word=""
#
#     for w in range (len(word1)-1, -1, -1):
#         new_word=new_word+word1[w]
#         print(new_word)
#
#     if word1==new_word:
#         return True
#     else:
#         return False
#
#
# print(is_palindrom("mom"))

# #4
# def if_pangram(sentence):
#     alphabet="abcdefghijklmnopqrstuvwxyz"
#
#     for char in alphabet:
#         if char not in sentence:
#             return False
#     return True
#
# print(if_pangram("quick brown fox jumps over the lazy dog"))

# #5
# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.islower():
#             result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#         elif char.isupper():
#             result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#         else:
#             result += char
#     return result
#
#
# message = "Hello, World! 123"
# shift = 3
# encrypted_message = caesar_cipher(message, shift)
# print("Encrypted:", encrypted_message)
#
#
# decrypted_message = caesar_cipher(encrypted_message, -shift)
# print("Decrypted:", decrypted_message)

# #6
# def modified_caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.islower():
#             result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#         elif char.isupper():
#             result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#         else:
#             result += char
#     return result
#
#
# message = "Hello, World! 123"
# shift=int(input("Enter number to shift the message:"))
# encrypted_message = modified_caesar_cipher(message, shift)
# print(encrypted_message)

# #7
# def compress_rle(data):
#     compressed_data = ""
#     i = 0
#     while i < len(data):
#         count = 1
#         while i + 1 < len(data) and data[i] == data[i + 1]:
#             i += 1
#             count += 1
#         compressed_data += data[i] + str(count)
#         i += 1
#     return compressed_data
# def decompress_rle(compressed_data):
#     decompressed_data = ""
#     i = 0
#     while i < len(compressed_data):
#         char = compressed_data[i]
#         count_str = ""
#         i += 1
#         while i < len(compressed_data) and compressed_data[i].isdigit():
#             count_str += compressed_data[i]
#             i += 1
#         count = int(count_str)
#         decompressed_data += char * count
#     return decompressed_data
# # Example Usage:
# input_data = "AAAAAABBBBCCDAA"
# print("Original Input Data:", input_data)
# # Compression
# compressed_data = compress_rle(input_data)
# print("Compressed Data:", compressed_data)
# # Decompression
# decompressed_data = decompress_rle(compressed_data)
# print("Decompressed Data:", decompressed_data)

# 8
import random
from sympy import mod_inverse
from sympy import isprime
def generate_keypair(bits):
  # Choose two large prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)
 # Calculate n
    n = p * q
 # Calculate φ(n)
    phi_n = (p - 1) * (q - 1)


  # Choose e
    e = choose_public_exponent(phi_n)
# Calculate d
    d = mod_inverse(e, phi_n)
    return ((e, n), (d, n))


def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Ensure the number has the correct bit

        if isprime(num):
           return num


def choose_public_exponent(phi_n):
 # Helper function to choose a public exponent e that is coprime to φ(n)
     e = random.randint(2, phi_n - 1)
     while gcd(e, phi_n) != 1:
         e = random.randint(2, phi_n - 1)
     return e


def gcd(a, b):
 # Helper function to find the greatest common divisor using Euclid's algorithm
    while b:
        a, b = b, a % b
    return a


def encrypt(message, public_key):
 # Encryption: C ≡ M^e (mod n)
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext


def decrypt(ciphertext, private_key):
 # Decryption: M ≡ C^d (mod n)
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message
 # Example Usage:


bits = 256
public_key, private_key = generate_keypair(bits)
message = "Hello, RSA!"
print("Original Message:", message)
# Encryption
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)
# Decryption
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
