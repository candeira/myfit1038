"At least it's not Moodle!"
===========================

**myfit1038** is a one-shot gdocs-spreadsheet-backed gae-hosted website for my fit1038 students at Monash to check their marks, and also an example of rapid app development for their unit.

- _one-shot_: though you may be able to tweak the code for your own purposes, it's far from a general solution.
- _gdocs-spreadsheet/backed_: using the very excellent [gspread](http://github.com/burnash/gspread "gspread") library by Anton Burnashev.
- _gae-hosted_: it's free (as in beer), also hassle-free (just upload and go!) and as Monash students have hosted gmail accounts, I get auth for free, erm, I don't have to set up my own auth.
- _for my fit1038 students_: If you are reading this far, I made this for you!
- _to check (their/your) marks_: if you aren't a student, I'm not telling you where the site is!
- _example of rapid app development_: the minimal website was up in 20 hours: 10 to go through the GAE tutorial and to learn how to use gspread, 5 to debug authorisation and other kinks, and 5 to debug and patch gspread. It took me longer to actually read and mark all the exams and reports.

How to install and run
----------------------

- Install [python2.7][python] and [git] on your computer.
- Install the python2.7 [Google App Engine SDK][sdk]. It comes with webapp2[wa2], which is the framework that myfit1038 uses.
- Fork this project and clone it from your own fork. You are going to have to modify it anyway. [Instructions at github][fac].
- Copy the gspread directory into your myfit1038 directory. GAE requires that you upload any non-standard and non-google provided library that you use.
- Register for a [Google App Engine][gae] account if necessary, and create a new application with whatever name you want.
- In the "Authentication Options", you can have "Open to all Google accounts" or "Open to all users with an OpenID provider". The app does its own access authorisation based on the emails listed in the spreadsheet. The "Storage Options" are irrelevant, since we 
- Configure the app by renaming "private.py.sample" to "private.py" and writing your own google docs account, password, spreadsheet name and list of emails of administrators.
- Here is a [sample spreadsheet][sample]. Copy it into your own gdocs account, and you can fill it with random values to start with. Use your fellow student's emails, play around with the grades!
- You can run the site locally using the gae dev_appserver or upload it to GAE using appcfg.py. If you don't know how, you better [follow the GAE tutorial][tutorial].

Good luck!


[git]: http://git-scm.com/
[python]: http://python.org/download/
[gae]: https://appengine.google.com/
[sdk]: 	https://developers.google.com/appengine/downloads
[fac]: http://help.github.com/fork-a-repo/
[sample]: https://docs.google.com/spreadsheet/ccc?key=0At_eoPQlRC9XdDZyMjJISTB2cGFuQXQweDQ2NWFzREE
[tutorial]: https://developers.google.com/appengine/docs/python/gettingstartedpython27/
=======
myfit1030 is a one-shot gdocs-spreadsheet-backed gae-hosted website for my fit1038 students at Monash to check their marks, and also an example of rapid app development for their unit.

- _one-shot_: though you may be able to tweak the code for your own purposes, it's far from a general solution.
- _gdocs-spreadsheet/backed_: using the very excellent gspread library by Anton Burnashev.
- _gae-hosted_: it's free (as in beer), also hassle-free (just upload and go!) and as Monash students have hosted gmail accounts, I get auth for free.
- _for my fit1038 students_: If you are reading this far, I made this for you!
- _to check (their/your) marks_: here you are!
- _example of rapid app development_: the minimal website was up in 20 hours: 10 to go through the GAE tutorial and to learn how to use gspread, 5 to debug authorisation and other kinks, and 5 to debug and patch gspread. It took me longer to actually read and mark all the exams and reports.
