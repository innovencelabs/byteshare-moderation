<p align="center">
  <img src="https://github.com/ambujraj/ByteShare/assets/29935993/17be8a31-71f3-4581-975c-9c1f6a8de2ef" alt="ByteShare logo" width="200" />
</p>
<h1 align="center">ByteShare Content Moderation</h1>

<p align="center">
    Content Moderation engine for ByteShare.
</p>

<p align="center">
    <img alt="GitHub License" src="https://img.shields.io/github/license/innovencelabs/byteshare-moderation">
    <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/innovencelabs/byteshare-moderation">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/innovencelabs/byteshare-moderation">
    <img alt="Static Badge" src="https://img.shields.io/badge/Pricing-Free-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/Join_Us-Contribute-red">
</p>

<p align="center">
    <img alt="Product Introduction" src="https://github.com/innovencelabs/byteshare/assets/29935993/2b004094-59b8-4e24-a0a4-6c9777b56b26">
</p>

## Local Setup
1. Clone the repository
```bash
git clone https://github.com/innovencelabs/ByteShare-Moderation.git
cd ByteShare-Moderation
```
2.  Add the credential values from your local ByteShare application in .env
```bash
cp .env.example .env
# Add your credentials in .env
```
3. Run the application through Docker Compose
```bash
docker compose up --build
```

#### Content Moderation will be started waiting for uploads.


## Built with
- Python
- Cloudflare R2
- RabbitMQ
