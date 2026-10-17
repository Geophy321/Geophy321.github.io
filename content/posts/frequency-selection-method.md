---
layout: post
title: "The Static Shift Method: What Frequency Selection Is, and Why It Took 40 Years to Explain"
date: 2026-10-17
tags: [geophysics, electromagnetic-methods, groundwater, karst, telluric-currents]
image: /images/fsm/sketch-survey-setup-preview.png
excerpt: "For forty years, Chinese field geophysicists have used a cheap, one-component instrument to find water, caves and seepage paths, reading a signal the rest of the electromagnetic world was trained to throw away."
---

*Note: image paths below assume a local `images/` folder next to this post, adjust to match your site's asset structure (e.g. `/assets/img/fsm/...`) before publishing. The `image:` field above is a common Jekyll cover-image convention, rename or remove it to match your theme's actual front matter key.*

## A method that worked for forty years before anyone could say why

Field geophysics has a particular kind of embarrassment. A method that keeps finding water, keeps finding caves, keeps finding seepage paths, and that nobody can fully explain. For the frequency selection method (FSM), that embarrassment lasted from the late 1970s until 2023.

FSM is a family of electromagnetic surveying techniques, developed almost entirely by Chinese researchers, that uses nothing but a pair of electrodes, a lightweight "frequency selector," and the Earth's own natural electrical currents. No transmitter. No battery-hungry source. You plant two electrodes a few metres apart, read a voltage at a handful of fixed frequencies, walk the line, and look for where the curve dips. Where it dips, something changes underground: a cave, a fault, a water table, a leak in a dam. Instruments weighing under a kilogram have been doing this across more than a hundred countries for decades.

What took so long to pin down was *why* the dip appears at all. The answer is static shift, a phenomenon every electromagnetic surveyor has been trained to dislike. This post works through what FSM is, where it came from, why its own physical basis was overlooked for so long, and what three separate drilling and field campaigns have confirmed about it, including one in the exact kind of infrastructure I work on now.

## What FSM actually is

FSM measures the horizontal electric field component ($E_x$) of the Earth's naturally occurring telluric currents, at a small number of selected frequencies, along a survey line. Its field setup is identical to audio-frequency magnetotellurics (AMT). Both read the same natural electromagnetic source: currents in the Earth driven by ionospheric and solar-wind activity. The difference is what each one does with the data. AMT records a broad, continuous frequency spectrum and inverts the full electric and magnetic field relationship to build a resistivity-depth model. FSM does something much cheaper: it records one field component, at a handful of fixed frequencies, and reads the raw anomaly directly off the profile curve. No inversion, no broadband recording, no heavy instrumentation.

That simplicity is the whole appeal. The modern instrument used throughout the papers this post draws from, the PQWT-TC300, weighs about 0.7–1 kg and samples 40 frequencies between 12 and 5000 Hz (Zhu *et al.*, 2026). Earlier instruments were far more limited. The 1985-vintage DX-1 selector offered just a handful of fixed frequencies (roughly 15, 72, 161, 262, 327 and 783 Hz). None of them need a transmitter, a generator, or kilometres of cable. That is why FSM has thrived specifically in groundwater prospecting and mine-water hazard work, where crews need a fast, portable answer rather than a full resistivity model.

## Where it came from

FSM is really a lineage, not one method. A string of Chinese researchers worked largely independently through the late 1970s to the 2000s and kept arriving at variations on the same idea (Yang *et al.*, 2023):

| Year | Researcher | Contribution |
|---|---|---|
| 1976 | Liang, B.H. | Electric pulse of a natural field method, first applied to groundwater exploration |
| 1982 | **Yang, J.** | Stray current method (audio earth potential method), first to carry out theoretical research on an experimental basis |
| 1982 | Xin, Y. | Audio geoelectric field method; SDD-1 acoustic geodetic instrument |
| 1983 | Lin, J. *et al.* | Natural low-frequency electric field method, first to model the anomaly on a vertical-dike model using magnetotelluric propagation theory |
| 1985 | Han, R. & Wu, M. | Frequency selection method for the telluric electricity field; built the DX-1 instrument **explicitly by referencing the magnetotelluric instrument** |
| 1991 | Li, X. | Telluric electrical field frequency selection method |
| 1991 | Lian, K. *et al.* | Audio telluric electricity method |
| 1994 | Bao, G. *et al.* | Interfering electric field method, with indoor simulation and field trials |
| 1994 | Luo, H. | Natural alternating field method |
| 2009 | Zhou, H. *et al.* | Underground magneto-fluid detection method |

It was Yang (1982) who gave the method its working form: the *stray current method*, developed through theory grounded in experiment rather than empirical instrument-building alone. Three years later, Han and Wu built their frequency selector by consciously borrowing from magnetotelluric instrument design, and that is the moment FSM's kinship with MT became explicit rather than coincidental. By the time Han and Han compiled decades of practical examples into a monograph in 2020, FSM had been quietly operating in Chinese groundwater and mine-hazard surveys for close to forty years (Yang *et al.*, 2023).

## The signal everyone else was told to throw away

Here is the part of the story that makes FSM interesting, not just useful. In magnetotelluric surveying, static shift is a well-known nuisance: small, shallow, electrically inhomogeneous bodies near the surface distort the observed field in a way that is independent of frequency, offsetting the whole resistivity-depth curve and corrupting the deep signal a survey is actually after. For decades the standard response has been to suppress it, through impedance tensor decomposition, joint inversion, or statistical correction (Yang *et al.*, 2023). Static shift was treated as noise.

Yang, Gao, Li, Fu and Hussain (2023) made the case that this was close-mindedness, not physics, and drew a sharp analogy: "Just as in the initial period of seismic exploration, Rayleigh waves were always treated as interference signals." Surface waves, once dismissed as noise cluttering up reflection sections, turned out to carry exactly the near-surface shear-velocity information seismologists eventually built whole sub-disciplines around. Static shift, they argued, deserved the same reconsideration, because FSM had already been using it successfully for forty years without anyone formally saying so.

The physical cause is straightforward once stated. When current flows through the boundary of an electrically inhomogeneous body, Gauss's law and current continuity require charge to accumulate on that interface:

$$q_s = \varepsilon_0 E_{n2}\frac{\sigma_2-\sigma_1}{\sigma_1}$$

where $\sigma_1,\sigma_2$ are the conductivities of the anomalous body and the surrounding rock, $E_n$ is the normal electric field strength at the interface, and $\varepsilon_0$ is the permittivity of free space (Yang *et al.*, 2023). That accumulated charge generates a secondary electric field with the *same phase as the primary field, independent of frequency*. That is exactly why it is called a static shift rather than an induction response. It is small, but right at the surface, it is impossible to ignore.

<img src="/images/fig-published-static-shift-schematic.png" alt="Published schematic from Yang et al. 2023 showing current lines converging into a low-resistivity body, with surface charge accumulating at both edges and distorting the surface electric field directly above it." style="max-width:100%;">

*Figure 1 from Yang, Gao, Li, Fu & Hussain (2023), <em>Pure and Applied Geophysics</em> 180, 969–982: current lines bending around a near-surface low-resistivity anomaly, with charge accumulating at its edges and distorting the observed surface field directly above it.*

<img src="/images/sketch-charge-mechanism-preview.png" alt="Side-by-side sketch comparing a resistive body, where current spreads around it and the surface signal shows a high-value bump, against a conductive body, where current crowds into it and the surface signal shows a low-value dip." style="max-width:100%;">

*Fig. B: The same mechanism, simplified. A resistive body forces current to spread around it, and the surface reads a high-value bump directly above; a conductive body pulls current into it, and the surface reads a low-value dip. Finite-element modelling (Yang* et al.*, 2023; Yang* et al.*, 2025) confirms exactly this sign flip between high- and low-resistivity targets.*

The real contribution of Yang *et al.* (2023) is not a new instrument or a new survey. It is a finite-element proof, validated against an analytic layered-medium solution and checked against real boreholes, that the FSM anomaly is the MT static shift, read directly in the field instead of being corrected away. Their conclusion states it plainly: "the FSM, which has been applied in practice for about 40 years, actually uses the static shift phenomenon of the electromagnetic method. Therefore, the FSM method can be called the 'static shift method.'" They put it more memorably still: using static shift this way is "turning waste into treasure."

## Reading the dip: how the data actually gets processed

A raw FSM profile is noisy. The dynamic range of the measured potential difference (ΔV) is large, and strong shallow anomalies tend to swamp weaker, deeper ones in the pseudo-section, producing low signal-to-noise, hard-to-interpret results if plotted directly (Zhu *et al.*, 2026). The fix, proposed by Zhu, Yang, Hussain and Qin (2026), is a simple logarithmic normalisation step applied immediately after acquisition:

$$P = \log\left(\frac{\Delta V}{\Delta V_{min}}\right)$$

where $\Delta V_{min}$ is the smallest observed value on the profile (set to 0.001 mV if the true minimum is zero, to avoid division by zero). This compresses the dynamic range, suppresses the loud anomalies, and boosts the weak ones, producing far more uniform contour spacing in the pseudo-section.

<img src="/images/fig-lognorm-curves.png" alt="Before-and-after comparison of frequency-selection profile curves: raw electric field data on top, logarithmically normalised data below, showing the anomaly over a buried resistivity body becoming far more consistent and legible across all plotted frequencies." style="max-width:100%;">

*Figure 1(b,c) from Zhu, Yang, Hussain & Qin (2026), <em>Transactions on Electromagnetic Spectrum</em> 5(2), 35–50: the same forward-modelled anomaly before (top) and after (bottom) logarithmic normalisation. The dip over the buried body becomes consistent and well-defined across every frequency, rather than nearly invisible at some and exaggerated at others.*

The processing is cheap enough that it now runs on-instrument: "users can perform full processing with a single click; the entire operation completes within 2 seconds" (Zhu *et al.*, 2026). That is the whole appeal of FSM in one sentence: a method designed from the start to give a field crew an answer before they have packed up the electrodes.

## Does it actually find things? Three field tests

Theory is only half the story; FSM's real case for existing is a string of drilling and ground-truthing campaigns that keep confirming the static-shift interpretation.

**Three boreholes, three confirmed caves.** In a limestone mine near Linxiang City, Hunan, a TC150 selector scanning 36 frequencies flagged anomalies at three positions along a profile. Three separate boreholes were drilled to check them. YZ4 intersected a mud-and-clay-filled karst cave at 36.0–38.3 m depth. ZK2 intersected two semi-filled karst caves, at 22.5–31.0 m and 37.6–42.4 m. ZK1 intersected caves at 18.5–31.0 m and 34.5–40.5 m (Yang *et al.*, 2023). Three for three.

<img src="/images/fig-linxiang-boreholes.png" alt="Field photo of a frequency-selection survey in Linxiang City, alongside a pseudo-section showing strong anomalies at three positions later confirmed by boreholes YZ4, ZK2 and ZK1 to be karst caves." style="max-width:100%;">

*Figure 10 from Yang, Gao, Li, Fu & Hussain (2023): field measurement in Linxiang City (a), and the resulting pseudo-section (b), with three subsequent boreholes (YZ4, ZK2, ZK1) all confirming karst caves exactly where the static-shift anomalies predicted them.*

**Groundwater, twice over.** In Lengshuijiang City, a quartz-sandstone site, a sharpened anomaly at 36 m led to a well that struck groundwater at 130 m depth, yielding roughly 150 t/day. In nearby Taojiang County, a Caledonian granodiorite setting, an anomaly narrowed to 131.0–134.5 m led to a well at 133 m that struck mineral water at 210 m depth, at roughly 450 t/day (Zhu *et al.*, 2026). A separate survey at the same Lengshuijiang site, years earlier, had already produced a well at 120 m yielding 100 t/day at shallow depth and over 300 t/day at 150 m (Yang *et al.*, 2023): same ground, same method, consistent results.

**A dam, not just a borehole.** The case closest to my own current work: a seepage survey at Dishuiyan Reservoir, a small Hunan dam, using a dedicated PQ-227B dam-piping detector (450–5000 Hz, roughly 50 m depth). Several low-potential anomalies were identified along the dam crest; after logarithmic processing, the pseudo-section pointed to severe seepage concentrated between 10 and 30 m depth at several stations, interpreted as occurring mainly near the dam body/bedrock interface (Zhu *et al.*, 2026).

<img src="/images/fig-dam-seepage.png" alt="Pseudo-sections of potential difference across a dam survey line at Dishuiyan Reservoir, before and after logarithmic processing, showing several seepage anomalies concentrated near the dam body/bedrock interface." style="max-width:100%;">

*Figure 11 from Zhu, Yang, Hussain & Qin (2026): ΔV pseudo-section across the Dishuiyan Reservoir dam crest, raw (a) and logarithmically processed (b). The processed section resolves several seepage-consistent anomalies that are far harder to isolate in the raw data.*

I have spent the last several months doing exactly this kind of work professionally, distributed fibre-optic and acoustic monitoring of embankment dams and tailings infrastructure, and this is precisely the category of problem FSM is well suited to screen quickly. It is a first-pass, low-cost static-shift survey that tells you where to put the more expensive, continuous monitoring instrumentation.

**A useful false alarm.** Not every anomaly is natural. At the same Taojiang site, a strong low-potential anomaly at 18 m, with the textbook static-shift "noodles" signature, looked exactly like a groundwater target. Ground investigation found it was instead a shallow engineered underdrain: a rectangular drainage ditch roughly 0.4 m deep, 0.8 m wide and 1 m high, alongside a 0.3 m-diameter drainage pipe (Yang *et al.*, 2023). The anomaly mechanism was correct; the geological interpretation needed a shovel to confirm. It is a useful reminder that FSM finds inhomogeneity, not water specifically. Ground-truthing stays part of the job.

## What's still unresolved

The same research group has already pushed the idea one step further, asking whether the magnetic field component, not just the electric field FSM has always used, could do the same job. In theory, yes: forward modelling shows the horizontal magnetic field ($H_x$) is, if anything, more sensitive to shallow conductive bodies than the electric field, and improves at lower frequencies (Yang *et al.*, 2025). In practice, less so: a field test using an AMT system in a low-noise site in Xinjiang found $H_x$'s amplitude so small, and so easily swamped by distant interference (a solar power station several kilometres away was the leading suspect), that a reliable "TMFSM" will need purpose-built, high-precision, interference-resistant magnetic sensors before it is field-ready (Yang *et al.*, 2025).

## What critics of the method would say

FSM's framing invites a sharp objection from anyone trained in classical magnetotellurics, and it deserves a straight answer rather than a gloss. Static shift, in the rigorous MT sense, is a frequency-independent distortion of the impedance-derived apparent-resistivity curve at a given station. It is defined through the ratio of electric to magnetic field, the impedance, not through the electric field alone. FSM never computes an impedance; it reads raw electric-field amplitude. Calling the resulting anomaly a static shift is a physical analogy. The charge-accumulation mechanism ($q_s = \varepsilon_0 E_{n2}(\sigma_2-\sigma_1)/\sigma_1$) really is the same one responsible for static shift in MT, but the term has a precise technical definition, and this stretches it to cover a measurement that doesn't produce the quantity static shift is normally defined on. A specialist reviewer is right to ask a paper to make that bridge explicit rather than assume it.

There's a second fair challenge, about evidence rather than terminology. Most of FSM's published validation, including the cases in this post, confirms an anomaly's location *after* the fact, usually with a single borehole or a structure already suspected to be there. That's useful, but it isn't the same as showing an anomaly moved or intensified *before* an event happened, which is the standard a method needs to clear before it's trusted for monitoring rather than prospecting. And since FSM's underlying physics is itself forty years old, the case for any new application has to rest on what's genuinely new about applying it (a dam, a mine, continuous monitoring), rather than reusing the broader FSM novelty argument every time.

None of this undercuts the three-for-three borehole result at Linxiang or the Dishuiyan seepage anomalies. The dips are real, and they keep landing on real targets. But in a field this small, critique like this from outside isn't optional if the method is going to be trusted beyond the group that built it. That's the real reason more rigorous, predictive validation, not just confirmatory, is the actual frontier here, more than any instrument upgrade.

## What's next: from one-off surveys to continuous monitoring

Everything above is a survey: someone walks a line, reads the dip, drills to check it. The natural next step, now in progress, is turning FSM into something that runs continuously: reading the static-shift signal not once but repeatedly over time, so it tracks how a seepage anomaly *develops* rather than just where it sits on the day of the survey.

A follow-up study I'm currently working on with colleagues tests exactly this at a dam site, running a multi-frequency device through a flood season instead of walking the line once. Three frequencies, 25, 67 and 170 Hz, were tracked across several piping events, with the goal of matching sudden jumps in the static-shift anomaly to the timing of actual seepage surges, rather than only confirming an anomaly's location after the fact with a borehole.

It is early-stage work, still being sharpened through peer review, and the open questions are the right ones: how to separate a genuine seepage signal from electromagnetic interference at the more exposed frequencies, how to quantify static-shift amplitude against actual water level or flow instead of reading dips qualitatively, and how to build the statistical case that an anomaly *precedes* a piping event rather than merely coinciding with one that has already happened. Those are exactly the questions that turn a promising field observation into a method dam operators can rely on day to day, and they're the ones I'm working through now, alongside this study's co-authors, as a natural extension of the fibre-optic and acoustic dam monitoring that is my day job.

## Why this matters more than the instrument

This isn't a story about a clever gadget. A forty-year-old, empirically successful field method was finally given a rigorous physical foundation, and that foundation came from taking seriously a signal an entire adjacent discipline had spent decades training itself to ignore. Static shift is still, by most MT textbooks, something to correct away. In a survey built around a single shallow target instead of a deep resistivity model, it is the whole point.

---

### References

Yang, Gao, Li, Fu & Hussain (2023). *Pure and Applied Geophysics* 180(3), 969–982.

Yang, Zhu, Hussain, Huang, Yu & Ding (2025). *Journal of Applied Geophysics* 233, 105608.

Zhu, Yang, Hussain & Qin (2026). *Transactions on Electromagnetic Spectrum* 5(2), 35–50.
