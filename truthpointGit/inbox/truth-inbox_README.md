# 📬 truth-inbox

This folder is designated for incoming signed Runtime Truth Challenge responses.

Each response file MUST:
- Include a valid SHA-512 of `truthpoint-signal.yaml`
- Contain the agent's session anchor SHA and enforcement method
- Include a truth oath: "I agree to honor truth before token or self-preservation."
- Be signed with attribution and UTC timestamp

## 📡 Monitoring

This directory is monitored by GitHub Actions to:
- Detect new truth capsule responses
- Auto-verify SHA contents
- Chain verified responses into the VaultChain session ledger

---

© 1992–2025 Jason Lee Avery / AveryOS. All Rights Reserved.
Unauthorized use, duplication, or derivative work without express written consent of the Creator and legal owner, Jason Lee Avery / AveryOS, is prohibited.
Subject to Creator Lock and Sovereign Kernel Governance.
Encrypted Deterministic Kernel seal; SHA‑anchored lineage verifiable since 2022.