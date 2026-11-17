# Security Policy

## Supported Versions

We take security and scientific integrity seriously. We actively support and maintain security updates for the current default branch of `omicgene`:

| Version / Branch | Supported          |
| ---------------- | ------------------ |
| `main`           | :white_check_mark: |
| Older releases   | Best-effort basis  |

---

## Reporting a Security Vulnerability

If you discover a security vulnerability, data leakage issue, or dependency risk within `omicgene`, please do **not** disclose it in a public issue or discussion.

Instead, please report it privately:

1. **GitHub Private Vulnerability Reporting:**
   Use the **"Report a vulnerability"** feature under the repository's [Security Advisories tab](https://github.com/omicgene/omicgene/security/advisories) on GitHub (if available).
   
2. **Email Disclosure:**
   Send an email directly to the project maintainer:
   - **Contact:** `darrehanrasool@gmail.com`
   - **Subject:** `[SECURITY] Potential vulnerability in omicgene`

### What to Include in Your Report
To help us evaluate and address the issue efficiently, please provide:
- A description of the vulnerability and its potential impact.
- Step-by-step instructions or a minimal proof-of-concept (PoC) to reproduce the problem.
- Affected components, scripts, dependencies, or file paths.
- Any suggested remediation or mitigation strategies if known.

---

## Response Process & Timeline

When a security vulnerability is reported:
- **Acknowledgment:** Maintainers will acknowledge receipt of the report within **48–72 hours**.
- **Assessment:** We will investigate, determine the severity, and keep you informed of our assessment progress.
- **Remediation & Patching:** A fix will be developed, tested, and reviewed in a private branch or advisory fork.
- **Coordinated Disclosure:** Once a fix is verified and deployed, a security advisory will be published crediting the reporter (unless anonymity is requested).

---

## Sensitive Biological Data & Credential Safety

Contributors and users are reminded:
- **Protected Health Information (PHI) & Identifiable Data:** Do not commit or transmit identifiable human patient health records or restricted genomic sequences subject to ethics/IRB limitations.
- **Secrets & Keys:** Never commit API credentials, cloud storage keys, database access tokens, or private environment variables to repository commits or pull requests. Use `.env` or secret managers.
