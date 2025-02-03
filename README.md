# workshop_malspam by Norwegian CERT for health and municipalities

This workshop is a hands-on introduction to malspam-investigation.

Included are real malwaresamples. Use appropriate caution. If you are unsure what appropriate caution is.. Ask a fried who does know, or find out ptherwise before starting.

## How to use

All cases use the same buildup. You start by unpacking stage1.7z. All stage1 samples are encrypted withthe password ```infected```.
Decryption can be done as follows.
```
$7z x stage1.7z -pinfected
```

### Your mission (should you choose to accept it)

The goal is to investigate the file within to determine:
1. Is it malicious?
If so find:
1. IOCs
    1. URLS / IPs
    2. filepaths
    3. regkeys
    4. other relevant IOCs to use for detection/remediation
2. Repeat this for all stages until you end up with either a congratulatory text-file, or a .exe/.dll.

### Tips and tricks

It is advised to:
- hash files before starting analysis. (keeps a clear trail, and helps detect unwanted alterations)
- note steps taken, and commands run for repeatability

### Follow on stages

If the folder contains a stage2.7z, og other variants they will always unpack with the downloadURL as the password.
E.g. stage2.7z for putty.msi would unpack as follows:
```$7z x stage2.7z -phttps://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.81-installer.msi```

## Intended order:
1. demo
    1. 1_powershell
    2. 2_vbs
    3. 3_lnk
    4. 4_doc
    5. 5_excel
    6. HTA
    7. bat
    8. JS
    9. onenote
    10. ppt
2. tasks
