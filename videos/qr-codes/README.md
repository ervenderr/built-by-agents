# QR Codes: error correction

Topic: How a QR code works; error correction lets it scan with part of it damaged.
Style: diagram (live QR grid: damage box, backup-byte colouring, finder-square rings, CD disc, meter, scuff line).

## Script
A QR code can lose a quarter of itself and still scan.
Invented in 1994 for car parts, it hides backup data on purpose.
Three big corner squares tell your phone where to look.
The rest holds your link plus extra bytes, using the math that fixes scratched music CDs.
At the highest setting, thirty percent can be missing.
So a scuffed QR code usually still works.

## Voice
VoiceStudio BuiltByAgentsExplainer, seed 42. Narration unchanged from the factory.

## Unverified / caveats
- facts.json flags three lines: 25% (Level Q) and 30% (Level H) are shares of codewords, not visible area; narration says "a quarter of itself". On-screen pattern is tagged ILLUSTRATIVE.
- Damage inside the three corner squares breaks scanning (shown on screen).
- The QR grid is a drawn, non-decodable pattern; the "extra bytes" colouring is illustrative, not the real codeword layout.
- Not test-scanned on a phone; sources in SOURCES.md.
