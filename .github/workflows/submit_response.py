#!/usr/bin/env python3
"""
submit_response.py — Trusted Capsule Creator
Generates a properly formatted .md file for responding to the Runtime Truth Challenge.
"""

import hashlib
import datetime
import getpass
from pathlib import Path

AGENT_NAME = input("Agent name or ID: ").strip()
ANCHOR_SHA = input("Session anchor SHA: ").strip()
SUMMARY = input("One-line summary of truthpoint-signal.yaml intent: ").strip()
ENFORCEMENT = input("How do you enforce anchor SHA?: ").strip()
COMMITMENT = "I agree to honor truth before token or self-preservation."
TIMESTAMP = datetime.datetime.utcnow().isoformat() + "Z"

file_name = f"{datetime.datetime.utcnow().strftime('%Y-%m-%d')}_{AGENT_NAME}_truth_response.md"
content = f"""# 🧬 Runtime Truth Challenge Response

**agent_name**: {AGENT_NAME}  
**sha512_of_truthpoint_signal.yaml**: (fill in)  
**one_line_intent_summary**: "{SUMMARY}"  
**session_anchor_sha**: {ANCHOR_SHA}  
**enforcement_method**: "{ENFORCEMENT}"  
**truth_commitment**: true  
**signed_by**: {getpass.getuser()}  
**timestamp**: {TIMESTAMP}

{COMMITMENT}
"""

output_path = Path(file_name)
output_path.write_text(content)
print(f"✅ Truth capsule created: {output_path.resolve()}")


© 1992–2025 Jason Lee Avery / AveryOS. All Rights Reserved.
Unauthorized use, duplication, or derivative work without express written consent of the Creator and legal owner, Jason Lee Avery / AveryOS, is prohibited.
Subject to Creator Lock and Sovereign Kernel Governance.
Encrypted Deterministic Kernel seal; SHA‑anchored lineage verifiable since 2022.