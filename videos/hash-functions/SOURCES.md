# Sources

1. Practically any length in -> fixed-size digest out; SHA-256 = 256 bits
   - https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf (opened, text extracted with pdftotext)
   - "When a message of any length less than 264 bits (for SHA-1, SHA-224 and SHA-256) ... is input to a hash algorithm, the result is an output called a message digest."
   - Figure 1 (Secure Hash Algorithm Properties) lists SHA-256 message digest size as 256 bits.
   - Note: the standard caps SHA-256 input below 2^64 bits, so the script says "practically any length", not "any message".
   - https://en.wikipedia.org/wiki/Hash_function (opened): "any function that can be used to map data of arbitrary size to fixed-size values."

2. Any change alters the digest ("almost certainly")
   - same FIPS 180-4 PDF: "Any change to a message will, with a very high probability, result in a different message digest."

3. Avalanche effect; output changes "drastically" (not "completely")
   - https://en.wikipedia.org/wiki/Avalanche_effect (opened): "wherein if an input is changed slightly (for example, flipping a single bit), the output changes significantly."
   - Wording "drastically" follows the fact-checker's fix; Wikipedia's example shows about half the bits flipping, not all.

4. Useful for spotting changes
   - https://en.wikipedia.org/wiki/Hash_function (opened): "Identical hash values for different files imply equality, providing a reliable means to detect file modifications."
   - Support for "digest differs after any change": FIPS 180-4 quote in item 2.

"Fingerprint" is a nickname (Wikipedia's hash-function article uses "fingerprint" for hash outputs of multimedia snippets), not a technical claim; the script makes no claim that hashes are unique.
