#!/usr/bin/env python3
import hashlib
import sys

EXPECTED_SHA = "b326020a5b58b51a1b62c5fbea93483303afee3dfbc5065e82dac71c84978479a39ad2bbe6783945c2ff426ea9d4a480c3b93e16f5a8759cc6cca2a60f0cc8de"

def compute_sha512(path):
    sha = hashlib.sha512()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            sha.update(block)
    return sha.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_external.py [path-to-kernel-file]")
        sys.exit(1)

    sha = compute_sha512(sys.argv[1])
    if sha == EXPECTED_SHA:
        print("✅ Verified: SHA-512 matches the public anchor.")
        sys.exit(0)
    else:
        print("❌ Verification failed.\nExpected:", EXPECTED_SHA, "\nGot     :", sha)
        sys.exit(2)
