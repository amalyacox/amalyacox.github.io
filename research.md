---
layout: page
title: Research
permalink: /research/
---

I am a 5th year PhD Candidate in the Stanford Materials Science & Engineering department co-advised by Professors [Fang Liu](https://sfrlab.netlify.app/) and [Aaron Lindenberg](http://web.stanford.edu/group/lindenberg/cgi-bin/drupal/). My work focuses on understanding and manipulating the thermal and excitonic properties of atomically thin or "two-dimensional" (2D) materials such as Graphene, or semiconducting transition metal dichalcogenides (TMDCs) like Molybdenum Disulfide (MoS<sub>2</sub>) and Tungsten Diselenide (WSe<sub>2</sub>). I develop new ways to fabricate these materials and use ultrafast optical experiments combined with computational modeling to understand the physical properties of these systems. The ultimate goal is to apply these materials to next-generation microelectronics for applications from clean energy, to quantum computing, to AI. 

### Tuning Thermal Transport through Morphology Engineering at Lawrence Berkeley National Laboratory 
As the global energy demand rapidly increases, developing energy efficient and sustainable energy sources will play a key role in mitigating the climate crisis. Thermoelectric (TE) devices are a promising source of clean energy as they can convert thermal energy from waste heat, which comprises 72% of global energy generated, back into electric power. Expanding the availability of TE devices and applying them to existing waste heat sources such as motors, hot water pipes, industrial equipment, computer servers, and more, can help significantly increase global production of and access to sustainable energy.

Recently, Two-Dimensional (2D) materials such as monolayer transition metal dichalcogenides (TMDs),  graphene, and SnSe have garnered interest for TE applications due to their low thermal conductivities, high and tunable Seebeck coefficients, tunable electrical conductivities, and relative affordability. In this project, we aim to tune the electrical and thermal conductivities of 2D materials through morphology engineering. Morphology engineering, which refers to the design and creation of nanometer sized bubbles or wrinkles, has a great potential to modulate the heat exchange, thermal insulation, and energy conversion properties of 2D materials. Our group has devised a lithography-free technique to engineer periodic nanoscale bubbles and wrinkles into monolayer materials. This designer approach can be used to control and realize new thermoelectric properties in a variety of thin materials, by controllably manipulating phonon and electron transport characteristics. The technique can be scaled for large scale production and commercialization, and will lead to the development of low-cost, flexible sustainable energy converters with the potential to be applied to a wide range of waste heat sources.

I was awarded a [DOE Office of Science Graduate Student Research Award](https://science.osti.gov/wdts/scgsr) to conduct part of this research at the Molecular Foundry at Lawrence Berkeley National Laboratory from July to September 2023, working with Dr. Archana Raja. I was awarded additional funding to continue this project from the [Stanford TomKat Center for Sustainable Energy](https://tomkat.stanford.edu/people/amalya-johnson). 

In this work, I have been developing a python package modeling nanoscale thermal transport in two-dimensional materials and thin films to be used for specific experimental techniques. The package will be published with the paper. 

![]('/images/aniso_thermaltransport.png)

### Ultrafast Electron Diffraction at SLAC National Laboratory 
Using ultrafast electron diffraction, I worked with a team of scientists at SLAC National Laboratory and Stanford to study thermal transport between monolayers in a multilayer stack. I fabricated large-area (mm-scale) monolayer materials and created heterobilayer stacks of these materials, which consists of one monolayer such as MoS<sub>2</sub> on top of another, such as WS<sub>2</sub>. In this experiment we photoexcited the system and used ultrafast electron diffraction to understand the time-resolved lattice dynamics upon photoexcitation. In this technique we obtain a series of diffraction images as a function of delay time, which can be used to understand atomic motion after photoexcitation. In this work we studied twisted TMDC heterostructures with type-II band alignments. The experiment produced over a TB of data in the form of diffraction images. For data analysis I built a python library to model the charge and heat transport in these heterostructures and simulate atomic reconstruction and diffraction of the layers. 

This work has been published [here](https://www.science.org/doi/10.1126/sciadv.adj8819), where we found resonant photoexcitation of the MoS(e)2 layer generated an anisotropic phonon distrubution that speeds up interlayer phonon-phonon transport from the MoS(e)2 layer to the WSe(2) layer. 

![]('/images/reconstruction_diffraction.png')
![]('/images/7N_test.png')
