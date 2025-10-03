DFIR Hackathon Challenge - WidgetCo Breach Investigation
Project Overview
This repository contains the results of a cybersecurity incident response investigation conducted during the WidgetCo DFIR Hackathon. The project involved triaging, analyzing, and reporting on a sophisticated multi-stage cyberattack that targeted the company's network.

The objective was to:

Reconstruct the attack timeline.

Identify Indicators of Compromise (IOCs).

Determine the scope and impact of the breach.

Provide actionable recommendations for containment, eradication, and recovery.

Final Report
The complete incident report is available in the DFIR_Report.pdf file. It details the full attack narrative, from the initial phishing attempt to the final data exfiltration and ransomware drop.

Key Findings

<img width="564" height="315" alt="image" src="https://github.com/user-attachments/assets/837a16d9-21ef-4453-983d-ae3651bb3ac6" />

<img width="580" height="290" alt="image" src="https://github.com/user-attachments/assets/539b8570-244c-4e16-bf20-3c1ea7bad051" />


The investigation revealed a highly coordinated attack campaign with the following key findings:

Initial Access: The attack vector was a targeted phishing email sent to multiple employees.

Compromised Accounts: The accounts of jsmith and jhipps were compromised, serving as the entry points.

Malicious Activity: The threat actor used legitimate Windows tools ("living off the land") such as powershell.exe, rundll32.exe, and regedit.exe to execute their malicious payloads.

Privilege Escalation: The attacker successfully escalated privileges by gaining membership in the Domain Admins group.

Data Exfiltration: Sensitive files were accessed and exfiltrated to external cloud services (Dropbox and Gist) before the final ransom note was deployed.

Persistence: The attacker established multiple persistence mechanisms, including a registry key and a scheduled task.
