"At least it's not Moodle!"
===========================

myfit1038 is a one-shot gdocs-spreadsheet-backed gae-hosted website for my fit1038 students at Monash to check their marks, and also an example of rapid app development for their unit.

- _one-shot_: though you may be able to tweak the code for your own purposes, it's far from a general solution.
- _gdocs-spreadsheet/backed_: using the very excellent [gspread](http://github.com/burnash/gspread "gspread") library by Anton Burnashev.
- _gae-hosted_: it's free (as in beer), also hassle-free (just upload and go!) and as Monash students have hosted gmail accounts, I get auth for free, erm, I don't have to set up my own auth.
- _for my fit1038 students_: If you are reading this far, I made this for you!
- _to check (their/your) marks_: if you aren't a student, I'm not telling you where the site is!
- _example of rapid app development_: the minimal website was up in 20 hours: 10 to go through the GAE tutorial and to learn how to use gspread, 5 to debug authorisation and other kinks, and 5 to debug and patch gspread. It took me longer to actually read and mark all the exams and reports.
