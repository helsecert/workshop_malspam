# workshop_malspam by the Norwegian CERT for health and municipalities

This workshop is a hands-on introduction to malspam-investigation.

Included are real malwaresamples. Use appropriate caution. If you are unsure what appropriate caution is.. Ask a fried who does know, or reconsider.

## Tools and setup

### Virtual machine
The demonstrations in the workshop will be based on a [Remnux VM](https://remnux.org/). When analysing anything malicious using a VM is best practice, and Remnux has the added benefit of being fairly light weight, and packed with many useful tools.

### Tools
In the tooling category the demonstrations will be based on the following (non-exhaustive) list of tools
- [VS Code](https://code.visualstudio.com/) (We want an editor with syntax highlighting)
- [7zip](https://www.7-zip.org/) included in Remnux
- [oletools](https://github.com/decalage2/oletools) included in Remnux
- [lnkinfo](https://github.com/libyal/liblnk/blob/main/lnktools/lnkinfo.c)
- [msidump](https://github.com/mgeeky/msidump) Tool to dump contents af MSI-files

It's possible to find substitutes for all these tools, but the demonstrations will be based on using them.
  
## How to use

Amlost all cases use the same Setup. You start by unpacking stage1.7z. All stage1 samples are encrypted with the password `infected`.
Decryption can be done as follows.
```
$7z x stage1.7z -pinfected

```
If stage2.7z, or something similar exists the password will always be the downloadURL.
E.g. stage2.7z for putty.msi would unpack as follows:
```$7z x stage2.7z -phttps://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.81-installer.msi```

One of the tasks works with ClickFix samples. The infratructure for that requires alloflisting of IPs. If samples appear down tell an instructor.

### Your mission (should you choose to accept it)

The goal is to investigate the file within to determine:
1. Is it malicious (Kepe in mind that some of the tasks might have benign samples!)?
If sample is malicious find:
1. IOCs
    1. URLS / IPs
    2. filepaths
    3. regkeys
    4. other relevant IOCs to use for detection/remediation
2. Repeat this for all stages until you end up with either a congratulatory text-file, or a .exe/.dll.
3. Some tasks has a `task.md`in those cases follow the specific tasks given there.
4. Some tasks have a `proposed-solution.md`. This file contains one possible solution. You should use this sparingly (either after doing all tasks, or if stuck)

### Tips and tricks

It is advised to:
- hash files before starting analysis. (keeps a clear trail, and helps detect unwanted alterations)
- Take note of steps taken and commands run for repeatability. The notes should be kept while working to avoid having to retrace steps a lot.


## Intended order:
1. demo
    1. 1_powershell/1,2,3,4 
    2. 2_vbs/1,2
    3. 3_lnk/
    4. 4_doc
    5. 5_EML
    5. 6_excel
    7. 7_HTML
    6. 8_HTA
    7. 9_onenote/1

2. tasks
    1. Start with 1, and move untill done :-) 

3. Bonus demos:
    1. 10_bat
    2. 11_JS
    3. 9_onenote
    4. 12_ppt
    5. 13_shellcode
