---
date: 2024-10-22
title: Lovers' Dew Case Study
description: A recounting behind the 3D modelling and rendering project for Matteo Parfums
---

In August 2024, I reached out to Matthew Sanchez on Twitter when he said that he was looking for a designer to produce high-quality 3D renders of his upcoming fragrance Lovers' Dew. This blog post is about the process behind the 3D modelling, the concept research phase and the execution for the whole project.

# Initial brief

This project involved creating six renders for Matteo Parfums' new fragrance called "Lover's Dew". The initial brief from the client included a written description of the creative direction and a few online references of existing fragrances and how each one advertised themselves on their respective marketing and online store.

The deliverables were six renders of the Lovers' Dew perfume bottle in two distinct categories: three e-commerce renders of the bottle on a white background and three more "beauty" images showcasing the perfume in more creative settings.

# 3D modelling in Plasticity

Since the client had already manufactured the perfume bottles, I thought that he had 3D models ready for me to use but that wasn't the case. Fortunately, he had provided me with some 2D drawing diagrams straight from the manufacturer for the glass bottle and the spray nozzle. So I was not worried about modelling these components accurately.

!()[media/lovers-dew/bottle-diagram.webp]

At first, I thought of modelling everything straight in Blender but the benefits of modelling in Blender (easier UV unwrapping, using the Blender modifiers) did not outweigh the benefits of modelling in Plasticity (peace of mind in terms of surface editability, surface quality and most important of all, accuracy).

I realized this very early on because the top profile of the glass bottle is made up of four intersecting circles of a radius equal to 60mm. If I wanted to make those four circles at the right radius (which is easy) but with the right number of vertices that that the intersection of each mesh circle overlap with another circle's vertices, that would have been a nightmare to calculate.

It is possible to make pretty accurate geometry using Blender. But the modelling process is flaky, involves more steps, isn't as accurate or flexible and leaves the door open for small mistakes such as moving a vertex by accident.

!()[media/lovers-dew/blender-modelling-issue-1.webp]

!()[media/lovers-dew/blender-modelling-issue-2.webp]

When I was thinking ahead at the amount of work it would take to make small changes to the dimensions or the amount of vertices in the main surfaces (and how it would affect bevels and subdivision surfaces down the line), I immediately committed to modelling everything in Plasticity.

Modelling in Plasticity was actually a fairly straightforward process. I know that in Plasticity, you cannot easily edit the G2 fillets like you can with the G1 fillets, so I resorted to creating many versions of the same geometry inside of the same file at each main step of the process.

!()[media/lovers-dew/overview-of-the-plasticity-file.webp]

I also very much enjoyed modelling small details that likely nobody would ever see such as the corkscrew for the spray nozzle on the neck of the glass bottle.


!()[media/lovers-dew/glass-screw-detail.webp]

When I got to the stage of modelling the spray nozzle, the client kindly provided the diagram for me.

!()[media/lovers-dew/diagram-nozzle-spray.webp]

Within a few minutes, I had a fully modelled accurate and editable spray nozzle.

!()[media/lovers-dew/spray-nozzle-detail-in-plasticity.webp]

## Correcting the mistakes in the vector logo

As for the marble cap with the embossed "MP" wordmark on top of it, I wanted to avoid the hassle and imprecision of doing it through a texture, so I decided to do it with real geometry with a boolean subtract. The client has his logo in a vector format but I noticed some slight inaccuracies in the vector artwork so I manually retraced the logo to get everything lined up correctly.

!()[media/lovers-dew/marble-cap-engraving-plasticity.webp]

Here were the differences between the provided vector artwork (in white) and the corrected version (the blue outline).

!()[media/lovers-dew/mp-logo-vector-corrections.webp]

The last detail I wanted to add with Plasticity was the liquid with the surface tension. With a quick boolean operation and fillet, I had everything I needed.

!()[media/lovers-dew/liquid-surface-tension-in-plasticity.webp]

And here is a screenshot of the important details from the finished model:

!()[media/lovers-dew/plasticity-finished-model.webp]

# Material shading in Blender

Now that I had everything related to the perfume bottle modelled, the next step was to figure out the material shaders for the various parts. Most important of which were the glass shader and the marble cap.

The goal was to use as many procedural material shaders as possible. They might be slower to render but they consume much less VRAM since they don't need to store all of the maps on there. Plus, the flexibility of tweaking every imaginable aspect of the shader is great when I or the client is looking for a specific look.

For the glass shader, I already had a pretty interesting look. It features a mix of three refractive shaders and one white glass shader.

!()[media/lovers-dew/glass-shader-setup.webp]

I also happened to have a very versatile procedural marble material in my Blender asset library.

!()[media/lovers-dew/marble-shader-setup.webp]

The only place where a texture had to be used was the front label of the glass bottle, showing "Lovers' Dew" and "MATTEO PARFUMS". I exported the UV layout of that front face from Blender and laid out the vector artwork in Affinity Designer 2.

!()[media/lovers-dew/front-bottle-texture.webp]

# The issue with compositing glass

After many attempts of rendering with a transparent background and using a background wall or ground geometry with "Shadow Catcher" and "Holdout" checked on in the Object properties, the compositor in Blender would not give me a pure white as a background although the "Set Alpha Over" node specifically used pure white! And since the "Set Alpha Over" node was after the adjustments made by the Render Raw add-on, I was extremely confused as to why I still didnt' get pure white on my background.

!()[media/lovers-dew/alpha-over-compositing.webp]

As shown with the example below with a green background for illustration purposes, the glass render does not have alpha values that show the green background to pass through it. So even if the workflow had been successful, it still wouldn't have solved all of my issues.

!()[media/lovers-dew/background-color-not-showing-through-glass.webp]

While working on this project, I also noticed that despite the recent improvements with the compositor, especially GPU compositing, there are still a few papercuts (dragging nodes is very laggy when the compositor is working on the viewport) and when working on many scenes like I did, Blender has the bad habit of displaying data objects like shaders, nodes and empties from other scenes - which was very annoying and confusing. For example, when trying to preview the "Viewer" Node inside of the Compositor, the Image Editor dropdown would display other viewer nodes and I never knew which one was which.

!()[media/lovers-dew/multiple-viewer-nodes-in-one-file.webp]

In the end, I had to give up on using the Compositor because it forced me to either:
- not have a perfect white background
- not have perfectly rendered shadows - the compositor would absolutely fudge those

Not to mention that sometimes, checking on the "Holdout" checkbox on the ground/wall geometry would inexplicably remove the shadow from the render. In conclusion, working with the compositor aside from doing color grading was a complete and utter nightmare because of the transparent glass.

# Research and moodboards

The client had provided about a half dozen references of existing work from established brands. I set out to create an extensive mood board in [PureRef](https://www.pureref.com/) to always refer to and share with the client.

!()[media/lovers-dew/pure-ref-overview.webp]

My initial ideas were to convey the serene qualities of water in various ways. I thought that doing proper fluid simulations was too ambitious and too deep of a rabbit hole for my very first attempt at this kind of work, so I looked at other ways of suggesting the presence of water.

After a bit of research and experimentation, I suggested to Matthew that we could go for a couple of underwater shots without doing fluid simulation, simply by using fake caustics and volumetrics.

!()[media/lovers-dew/water-references-in-pureref.webp]

The overall shots could be enhanced with various props and lighting tricks such as volumetrics, light rays, particles and caustics.

But the initial ambition with the client was to use 3D models that represented the tones of the fragrance. To save time for the approval of the creative direction, I used the Flux generative AI model on [Fal.ai](https://fal.ai/). If you're interested, here are the links to the [Schnell model](https://fal.ai/models/fal-ai/flux/schnell) and the [Pro model](https://fal.ai/models/fal-ai/flux-pro).

!()[media/lovers-dew/flux-schnell-screenshot.webp]

I started using these inspiration shots to make the initial sketch renders but I still wanted to have more suggestions and stumble on happy accidents along the way. One of the many tools I used to do that was [Supercraft AI](https://supercraft.ai/). I found out about it while working on this project stumbled on [their YC launch page](https://www.ycombinator.com/companies/supercraft), so I immediately joined the Supercraft AI Discord server, gave some feedback about the product and Sarang the CEO reached out through a call to find out more.

!()[media/lovers-dew/supercraft-ai-screenshot.webp]