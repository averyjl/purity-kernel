#!/bin/bash
echo "Verifying SHA-512 for pk-core_bundle.zip"

if sha512sum -c pk-core_bundle.sha512; then
    echo "✅ Integrity check passed"
else
    echo "❌ Integrity check failed"
fi