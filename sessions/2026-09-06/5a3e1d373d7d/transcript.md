

---

## Attachment: a4faba724217479f8a4127ead8e0bd50.jpg

| Field | Value |
|-------|-------|
| **Type** | Image |
| **Filename** | a4faba724217479f8a4127ead8e0bd50.jpg |
| **Received** | 2026-09-06T00:08:16Z |

### Extracted Text

```
Bugsnag alert email (screenshot a4faba724217479f8a4127ead8e0bd50.jpg):

- App: [krake_ror]
- Error: Errno::ENOSPC in krakes#check
- Request URL: https://getdata.io/community/data-sources/check
- Meaning: No space left on device — disk full on the krake_ror Rails host.

RESOLUTION (2026-09-06 ~00:06 UTC):
- Root cause: /home/ubuntu/krake_ror/log/production.log grew unbounded until the 7.8G root volume hit 100%. No logrotate config existed. Puma (PID 1533, started Sep 02) held a 3,983,423,744-byte (3.98GB) DELETED production.log inode open — du/df gap ~3.6GB; space was unreclaimable until process restart.
- Fix: sudo service krake_ror restart → freed inode; df / 100% → 53% (3.5G avail). App healthy: HTTP 200 in 0.117s locally; ALB krake-ror-1 target i-085896f3427372e0a healthy.
- Recurrence prevention: wrote /etc/logrotate.d/krake_ror (daily + size 200M, rotate 5, copytruncate, delaycompress, su ubuntu ubuntu); force-run verified rotation (production.log → production.log.1 864K). Cron running on host.
- Host inventory correction: current krake_ror = i-085896f3427372e0a, 54.205.127.43, 172.31.17.3, t2.micro, us-east-1c, ASG krake_ror (Min=Max=Desired=1, launch template lt-085100be44b6079cc v3, no BlockDeviceMappings → 8G root), ELB health ELB, target group krake-ror-1:3002. Launched 2026-09-02 06:17 (ASG had already recycled the ENOSPC box once). SSH key GETDATA_key_pair (server_us.pem); needs PubkeyAcceptedKeyTypes=+ssh-rsa.
- NOTE: logrotate conf is host-local — a future ASG recycle loses it (LT has no user-data). Durable fix = add user-data/bootstrap to launch template or bake into AMI. Volume also small (8G) — consider grow to 20G+ if traffic keeps growing (log ~13KB/s ≈ 1.1GB/day, mostly normal request logging).
```

### OCR Result

```
[krake_ror] Errno::ENOSPC in krakes#check — VIEW ON BUGSNAG — request URL https://getdata.io/community/data-sources/check
```
