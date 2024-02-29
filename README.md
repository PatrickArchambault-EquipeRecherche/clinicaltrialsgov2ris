# clinicaltrialsgov2ris
Convert the CSV output from https://clinicaltrials.gov/ to RIS

Converting the CSV (Comma-Separated Values) from clinicaltrials.gov to RIS requires a number of tradeoffs.

First, we are converting a trial registration to a citation for a Journal Article, which is not a great fit. It does make it easy to import into Reference Management and Systematic Review Screening tools, so that was the choice.

Second, we have to decide which Fields from the trial registration to include, and which RIS field they should correspond to.

Here are the choices made:

|CSV Heading | RIS Field|
|--------------------|--------------------|
|NCT Number | DOI|
|Study Title | TI (Title)|
|Study URL | UR (URL)|
|Acronym | J2 (Alternate Title)|
|Brief Summary | AB (Abstract)|
|Interventions | U1 (Notes 1)|
|Study Design | U2 (Notes 2)|
|Completion Date | YR (Publication Year)|
|Study Documents | L1 (File Attachments)|

I am also adding "clinicaltrials.gov" as a DB field (Database), and todays date as an RD field (Retrieved Date).