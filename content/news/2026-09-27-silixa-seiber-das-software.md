Title: Working with commercial DAS software: Silixa SeiBer
Date: 2026-09-27
Summary: Setting up Silixa's SeiBer software for DAS processing on active-source MASW surveys on embankment dams.
Cover: images/seiber_sketch.png

For about ten years I have worked mostly with open-source code. It gave me flexibility and a deep understanding of the methods, but as my work has moved from academic to industrial research, I have started using commercial software as well. In operational monitoring, stability and well-tested tools matter as much as flexibility.

Recently I have been setting up Silixa's SeiBer software for distributed acoustic sensing (DAS) processing. The workflow covers configuration of the iDAS and iDAS-M interrogators, conversion of native TDMS files to SEG-Y, and assignment of hammer (shot) positions along the survey line for active-source MASW surveys on embankment dams.

Getting it running was not plug-and-play, and I learned a lot from that. SeiBer is built from several parts that depend on each other: a backend that handles data conversion, a web-based frontend for the user interface, and a MongoDB database underneath. When the interface would not start, the error message gave little to go on, so I worked through the system one layer at a time: checking the database, then the backend, then the frontend. That pointed to a compatibility issue between components rather than a fault in any single one.

It was a useful reminder that commercial software still depends on its environment, and that knowing how the parts fit together makes troubleshooting much faster. I appreciated the support from Silixa's software development team along the way and look forward to using SeiBer in upcoming dam monitoring work.
