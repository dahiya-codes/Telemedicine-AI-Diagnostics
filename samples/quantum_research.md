# The Impact of Quantum Computing on Modern Cryptography

## Executive Summary

Quantum computing represents the most significant threat to modern cryptographic infrastructure since the invention of public-key cryptography in the 1970s. The mathematical foundations underpinning RSA, ECC, and Diffie-Hellman key exchange — algorithms protecting trillions of dollars in global financial transactions, government communications, and personal data — are provably vulnerable to quantum attacks. Shor's algorithm, running on a sufficiently powerful quantum computer, can factor large integers and solve discrete logarithm problems in polynomial time, rendering today's asymmetric encryption obsolete.

The urgency is compounded by the "harvest now, decrypt later" threat: adversaries are already collecting encrypted data today with the intent to decrypt it once quantum computers reach sufficient capability. Sensitive data with long secrecy requirements — state secrets, medical records, intellectual property — is already at risk. NIST's post-quantum cryptography standardization process, completed in 2024, marks the beginning of a global cryptographic migration that will take decades and cost hundreds of billions of dollars.

## Current State of Quantum Computing

### Hardware Progress and Timelines

Quantum computing hardware has advanced dramatically over the past decade. IBM's Condor processor reached 1,121 qubits in 2023, while Google's Sycamore demonstrated quantum supremacy in 2019 by completing a specific computation in 200 seconds that would take classical supercomputers 10,000 years. However, raw qubit count is misleading — current quantum computers are NISQ (Noisy Intermediate-Scale Quantum) devices with error rates too high for cryptographically relevant computations.

Breaking RSA-2048 requires approximately 4,000 logical qubits with error correction, translating to roughly 4 million physical qubits given current error rates of 0.1-1%. Most experts estimate cryptographically relevant quantum computers (CRQCs) are 10-15 years away, though some assessments place the timeline as early as 2030. The uncertainty itself is a risk management challenge for organizations planning cryptographic transitions.

### Key Players and Investment Landscape

Global investment in quantum computing exceeded $35 billion in 2022, with governments accounting for over $22 billion. The US National Quantum Initiative has committed $1.8 billion through 2023. China's quantum investment is estimated at $15 billion, with significant focus on quantum communications and cryptography. The EU Quantum Flagship program has allocated €1 billion over 10 years.

Major technology companies including IBM, Google, Microsoft, Intel, and IonQ are competing across different hardware approaches: superconducting qubits, trapped ions, photonic systems, and topological qubits. Each approach has distinct error rate, coherence time, and scalability trade-offs that will determine which platform first achieves cryptographic relevance.

## Cryptographic Vulnerabilities

### Asymmetric Encryption at Risk

Public-key cryptography relies on mathematical problems believed to be computationally hard for classical computers. RSA security depends on the difficulty of factoring large integers — a 2048-bit RSA key would take classical computers longer than the age of the universe to break. Shor's algorithm reduces this to hours on a sufficiently powerful quantum computer.

Elliptic Curve Cryptography (ECC), used in TLS, SSH, Bitcoin, and most modern secure communications, is equally vulnerable. The elliptic curve discrete logarithm problem, which provides ECC's security, is also efficiently solvable by Shor's algorithm. A 256-bit ECC key provides equivalent classical security to a 3072-bit RSA key, but both fall to the same quantum attack.

### Symmetric Encryption and Hash Functions

Symmetric encryption algorithms like AES and hash functions like SHA-256 are significantly more quantum-resistant. Grover's algorithm provides a quadratic speedup for searching unsorted databases, effectively halving the security level of symmetric keys. AES-128 would be reduced to 64-bit effective security — insufficient — while AES-256 would retain 128-bit effective security, considered adequate.

SHA-256 and SHA-3 hash functions retain approximately half their classical security against quantum attacks, meaning SHA-256 provides roughly 128-bit post-quantum security. This makes hash-based cryptographic constructions particularly attractive as quantum-resistant building blocks for digital signatures and key derivation.

### Protocols and Infrastructure at Risk

The vulnerability extends far beyond individual algorithms to entire protocol stacks. TLS 1.3, which secures HTTPS traffic, uses ECDHE for key exchange and ECDSA for authentication — both quantum-vulnerable. IPsec VPNs, SSH, PGP email encryption, code signing certificates, and blockchain systems all rely on quantum-vulnerable asymmetric cryptography.

Critical infrastructure including power grids, financial systems, healthcare networks, and government communications depends on these protocols. The attack surface is enormous: over 1 billion websites use TLS, and the global PKI infrastructure issues hundreds of millions of certificates annually, all of which will require replacement in a post-quantum world.

## Post-Quantum Cryptography Solutions

### NIST Standardization Process

NIST's Post-Quantum Cryptography Standardization project, launched in 2016, evaluated 82 candidate algorithms across four rounds of analysis. In 2024, NIST finalized four standards: CRYSTALS-Kyber (ML-KEM) for key encapsulation, CRYSTALS-Dilithium (ML-DSA) and FALCON (FN-DSA) for digital signatures, and SPHINCS+ (SLH-DSA) as a hash-based signature alternative.

These algorithms are based on mathematical problems believed to be hard for both classical and quantum computers: lattice problems (Learning With Errors, Module-LWE), hash functions, and code-based cryptography. The diversity of mathematical foundations provides defense-in-depth against future algorithmic breakthroughs.

### Lattice-Based Cryptography

Lattice-based cryptography has emerged as the dominant post-quantum paradigm, underpinning three of the four NIST standards. The security of lattice schemes rests on the hardness of problems like Learning With Errors (LWE) and its variants, which have resisted decades of classical and quantum cryptanalysis. Lattice schemes offer practical performance characteristics — key sizes and computation times comparable to current RSA and ECC implementations.

CRYSTALS-Kyber provides key encapsulation with public keys of approximately 800 bytes and ciphertexts of 768 bytes for the 128-bit security level, compared to 256 bytes for a 256-bit ECC public key. The modest size increase is manageable for most applications, though bandwidth-constrained IoT devices and embedded systems face more significant challenges.

### Hash-Based and Code-Based Alternatives

SPHINCS+ provides a conservative post-quantum signature scheme based solely on the security of hash functions, offering strong security guarantees with minimal assumptions. Its primary drawback is signature size — approximately 8KB for the 128-bit security level — making it unsuitable for bandwidth-sensitive applications but ideal for high-assurance use cases like firmware signing and certificate authorities.

Code-based cryptography, based on the hardness of decoding random linear codes, has the longest history of post-quantum cryptanalysis with no known quantum speedups beyond Grover's algorithm. Classic McEliece, a code-based key encapsulation mechanism, was a NIST finalist and remains a conservative alternative despite its large key sizes of 261KB.

## Migration Challenges and Strategic Recommendations

### Cryptographic Agility and Inventory

The first step in any post-quantum migration is cryptographic inventory — identifying all systems, protocols, and data stores that rely on quantum-vulnerable algorithms. This is a significant undertaking for large organizations with complex IT estates. Automated discovery tools are emerging to scan codebases, network traffic, and certificate stores for quantum-vulnerable cryptographic usage.

Cryptographic agility — designing systems to swap cryptographic algorithms without architectural changes — is essential for managing the transition. Organizations that have hardcoded specific algorithms into protocols and hardware face the most difficult migration paths. The lesson from SHA-1 and MD5 deprecation is that cryptographic transitions take far longer than anticipated.

### Hybrid Cryptography as a Bridge

Hybrid cryptographic schemes combining classical and post-quantum algorithms provide a pragmatic transition strategy. A hybrid TLS handshake using both ECDHE and Kyber key exchange ensures security against both classical and quantum adversaries during the transition period. Google, Cloudflare, and Amazon have already deployed hybrid post-quantum TLS in production.

The performance overhead of hybrid schemes is modest — Kyber adds approximately 1-2ms to TLS handshake times in typical deployments. This overhead is acceptable for most applications and provides immediate protection against harvest-now-decrypt-later attacks while the ecosystem transitions to pure post-quantum implementations.

### Timeline and Investment Requirements

Organizations should prioritize migration based on data sensitivity and longevity. Data requiring confidentiality beyond 2030 should be protected with post-quantum encryption today. Critical infrastructure and government systems should target post-quantum migration completion by 2027-2028. Consumer-facing applications have more flexibility but should plan for post-quantum TLS deployment by 2026.

Global post-quantum migration costs are estimated at $7-10 billion for the financial sector alone, with total global costs potentially exceeding $100 billion when hardware replacement, software updates, and operational costs are included. Early movers will benefit from lower costs and reduced risk exposure compared to organizations that delay migration.

## Future Outlook

### Quantum Key Distribution

Quantum Key Distribution (QKD) uses quantum mechanical properties to distribute cryptographic keys with information-theoretic security — any eavesdropping attempt disturbs the quantum states and is detectable. China's Micius satellite demonstrated intercontinental QKD over 7,600km in 2020. The EU Quantum Internet Alliance is developing a pan-European quantum network targeting deployment by 2030.

QKD's practical limitations — requirement for dedicated fiber or line-of-sight optical links, distance constraints, and high infrastructure costs — restrict its applicability to high-value point-to-point links rather than general internet security. Post-quantum cryptography will remain the primary solution for securing internet communications.

### Long-Term Cryptographic Landscape

The post-quantum transition will reshape the cryptographic landscape for decades. Quantum-resistant blockchain systems, post-quantum secure enclaves, and quantum-safe hardware security modules are already in development. The intersection of quantum computing and AI creates new attack vectors — quantum machine learning algorithms may accelerate cryptanalysis in ways not yet fully understood.

- NIST post-quantum standards finalized in 2024: ML-KEM, ML-DSA, FN-DSA, SLH-DSA
- RSA and ECC broken by Shor's algorithm on cryptographically relevant quantum computers
- Harvest-now-decrypt-later attacks make migration urgent for long-lived sensitive data
- AES-256 and SHA-256 retain adequate security with doubled key/output sizes
- Global migration costs estimated at $100B+ over the next decade
- Hybrid post-quantum TLS already deployed by Google, Cloudflare, and Amazon
