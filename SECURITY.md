# 🔒 Security Policy

## 📌 Supported Versions

The following versions of Zero Touch Music currently receive security updates:

| Version | Supported          |
|---------|-------------------|
| Latest  | ✅ Yes             |
| Older versions | ❌ No      |

Please ensure you are using the latest version before reporting vulnerabilities.

---

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability, **please do not open a public issue**.

Instead, report it responsibly by emailing:

📧 zerotouchai.official@gmail.com  

Include the following details:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Screenshots or logs (if applicable)
- Suggested fix (if available)

You will receive acknowledgment within 48 hours.

---

## 🔐 Security Best Practices

When using Zero Touch Music:

- Keep your YouTube API credentials secure.
- Never commit API keys, OAuth secrets, or email passwords.
- Use environment variables for sensitive information.
- Enable 2-factor authentication on your Google account.
- Use app-specific passwords for SMTP access.
- Regularly rotate API keys and credentials.

---

## 🛡 Handling Sensitive Data

This project may require:

- YouTube API credentials
- OAuth client secrets
- Email SMTP credentials

Store these securely:

- Use `.env` files (never commit them)
- Add `.env` to `.gitignore`
- Use environment variables in production

Example:

```bash
export YOUTUBE_CLIENT_SECRET="your_secret_here"
export EMAIL_PASSWORD="your_password_here"
```

---

## ⚠️ Responsible Disclosure

We appreciate responsible disclosure of security issues.

- Do not exploit vulnerabilities.
- Do not access data that is not yours.
- Do not publicly disclose the issue until it has been resolved.

We will work quickly to investigate and patch confirmed vulnerabilities.

---

## 🔄 Security Updates

Security patches will be released as soon as possible after confirmation.  
Users are encouraged to update immediately once a patch is published.

---

Thank you for helping keep Zero Touch Music secure.
