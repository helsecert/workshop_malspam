# workshop_malspam_First_TC_Oslo_2024

This workshop is a hands-on introduction to malspam-investigation.

Included are real malwaresamples. Use appropriate caution. If you are unsure what appropriate caution is.. Ask a fried who does know, or stay away.

## How to use
Alle cases use the same buildup. You start by unpacking stage1.7z. All stage1 samples are encrypted withthe password ´infected´.
Decryption CAN be done as follows.
$7z x stage1.7z -pinfected
### Your mission (should you choose to accept it)
The goal is to investigate the file within to find:
1. IOCs
    1.1. URLS / IPs
    1.2. filepaths
    1.3. regkeys
    1.4. other relevant IOCs to use for detection/remediation
2. Repeat this for all stages until you end up with either a congratulatory text-file, or a .exe/.dll.

### Tips and tricks
It is advised to:
- hash files before starting analysis. (keeps a clear trail, and helps detect unwanted alterations)
- note steps taken, and commands run for repeatability

### Follow on stages
If the folder contains a stage2.7z, og other variants they will always unpack with the downloadURL as the password.
E.g. stage2.7z for putty.msi would unpack as follows:
´$7z x stage2.7z -phttps://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.81-installer.msi´

