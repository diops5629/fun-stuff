### Three's a Crowd
I thought that XOR ciphers were kind of fun, so why not try the same thing with ternary instead of binary?
Works on the same principles, probably has a butt-ton of vulnerabilities, but hey, this is for fun. Honestly, this probably has the same vunerabilities as a XOR cipher. Also, yes, this implementation is inefficient and messy as heck. There's no comments in my implementation, so if you want me to comment on it, please send me a message, otherwise I'm going to forget.

How it works:
A-Z correspond to 0-25,
Space corresponds to 26,
Works like this:

Convert to base 3, then add the characters together. The output is the digit in the 'ones' place.

Example:

Message = "E", Key = "C"
Convert to ternary
Message = 011, Key = 002
XOR Operation
1st character: M = 0, K = 0, Output = 0+0=0
2nd character: M = 1, K = 0, Output = 1+0=1
3rd character: M = 1, K = 2, Output = 1+2=10=0

Encrypted Message = 010
Convert back to character,
Encrypted message is "D"

To decrypt
1st character: M = 0, K = 0, Output = 0-0=0
2nd character: M = 1, K = 0, Output = 1-0=1
3rd character: M = 0, K = 2, Output = 10-2=1

Negatives aren't used in decryption, so assume it works like an overflow. 0-1 -> 10-1 = 2

The implementation only takes lowercase. 

I wonder if anyone's going to read this.
