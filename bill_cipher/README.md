### Three's a Crowd
I thought that XOR ciphers were kind of fun, so why not try the same thing with ternary instead of binary?
Works on the same principles, probably has a butt-ton of vulnerabilities, but hey, this is for fun. Ternary works somewhat since all letters of the alphabet plus a space is 27 characters. Also, yes, this implementation is inefficient and messy as heck. There's no comments in my implementation, so if you want me to comment on it, please send me a message, otherwise I'm going to forget.

How it works:
A-Z correspond to 0-25,
Space corresponds to 26,
Works like this:

Convert message to ternary, then do the "xor" on it between message and key.
If the message and key are both the same character, then output the same character.
If the message and key are different, use the excluded characters.
Example:

Message = "E", Key = "C"
Convert to ternary
Message = 011, Key = 002
XOR Operation
1st character: M = 0, K = 0, Output = 0
2nd character: M = 1, K = 0, Output = Excluded character = 2
3rd character: M = 1, K = 2, Output = 0

Encrypted Message = 020
Convert back to character,
Encrypted message is "G"

The implementation only takes lowercase. 

I wonder if anyone's going to read this.
