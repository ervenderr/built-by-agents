# Sources

All from RFC 8446 (TLS 1.3), https://www.rfc-editor.org/rfc/rfc8446 (opened; first 100k chars read: sections 1-2). Cloudflare page returned 403, not used.

1. Line 1 (secure over a public channel; key agreement)
   - "Data sent over the channel after establishment is only visible to the endpoints."
   - Handshake "negotiates cryptographic modes and parameters, and establishes shared keying material."
2. Line 2: "the client sends the ClientHello"
3. Line 3: "the ServerHello contains a "key_share" extension with the server's ephemeral Diffie-Hellman share"
4. Line 4: "The combination of the ClientHello and the ServerHello determines the shared keys."
5. Line 5
   - "The certificate of the endpoint and any per-certificate extensions."
   - "A signature over the entire handshake using the private key corresponding to the public key in the Certificate message."
6. Line 6: "All handshake messages after the ServerHello are now encrypted." and "Data sent over the channel after establishment is only visible to the endpoints."
