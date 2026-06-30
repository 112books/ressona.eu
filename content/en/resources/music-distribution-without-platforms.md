---
title: "Distributing your music without platforms: full sovereignty"
description: "Your own website, direct downloads, RSS, Faircamp, Funkwhale. How to publish music without giving a cent to big platforms and keeping full control of everything."
translationKey: "blog-diy-music-distribution"
type: resources
date: 2026-06-30
draft: true
author: "Ressona"
tags: ["digital-tools", "musicians", "distribution"]
category: distribucio
---

Some artists don't want to give a single cent to Spotify, Apple or Amazon. By principle or by strategy. They want their fans to access their music directly — no intermediaries, no algorithms, no data trails ending up at a corporation.

It's possible. It takes a little more upfront effort, but the control you gain is total.

## The base principle: your website as distribution point

If you have your own website on your own domain, you already have 90% of the infrastructure you need to distribute music independently. An MP3 or FLAC file uploaded to your server is, technically, direct distribution.

What you need to add on top:

- **A page for each release** with information, artwork and a download or play button
- **An optional payment system** if you want to charge (Stripe, Ko-fi, or simply a bank account number)
- **A mailing list** to notify fans when new music drops

With these three elements you have a complete independent distribution infrastructure.

## Faircamp: the free Bandcamp

[Faircamp](https://codeberg.org/simonrepp/faircamp) is a static site generator for musicians — essentially what Bandcamp should be if it were free software. You host it yourself (or have someone set it up for you), but once it's running it works on its own.

**What Faircamp does:**
- Automatically generates a website for your releases from a folder structure
- Supports downloads in multiple formats (MP3, FLAC, OGG, OPUS)
- Allows sales with coupon codes and password-controlled access
- Runs without a database or PHP — pure HTML
- Supports multiple artists or labels

**Who funds it:** the European Commission's NGI0 Entrust programme, through NLnet. No company with shareholders behind it. Version 1.0 published in 2024.

**Requirement:** web hosting (any basic server works) and someone to configure the system initially. After that, adding music is as simple as copying folders.

## Funkwhale: the federated radio

[Funkwhale](https://funkwhale.audio/) is a federated, open-source streaming platform, part of the Fediverse (the same ecosystem as Mastodon and Pixelfed). It works like Spotify but without the company, without algorithms, and without data going anywhere.

**Usage options:**
- **Your own instance**: you host your Funkwhale, you control everything. Requires a server and technical knowledge (or someone to set it up).
- **Community instances**: you can join an existing instance managed by a community without hosting anything. Instances federate with each other.

**For whom:** independent labels, music collectives, artists with a community focus. It's not a mass discovery platform — it's a tool for an audience that already loves your work and prefers federated alternatives.

## RSS: invisible distribution

RSS is the oldest and most robust subscription protocol on the internet. Podcasts use it. And music is, technically, audio — which is exactly what RSS can distribute.

If you publish your music with an RSS feed (any website can generate one), your fans can subscribe with any podcast app (Pocket Casts, AntennaPod, Overcast) and receive each new release automatically, without any intermediary platform.

Some podcast apps even download episodes automatically. This is exactly what many experimental music artists and netlabel releases already do.

**How to implement it:** any Hugo, WordPress or similar website generates RSS feeds automatically. If you publish your songs as blog posts with the audio file attached, you have a working music feed.

## Direct download with voluntary payment

The "pay what you want" model that Bandcamp popularised isn't Bandcamp's property. You can implement it on your own website with simple tools:

- **Ko-fi**: direct support platform. Allows "buying" an album and receiving the file as a download. Ko-fi charges 0% if you use Stripe directly (Stripe charges its standard fee of ~1.4% + €0.25).
- **Stripe Payment Links**: generate a payment link for a product (your album) and send the file by email once the transaction completes.
- **Gumroad**: digital product sales platform. Charges 10% per transaction but is very easy to use.
- **Free direct download**: simply a link to a ZIP file on your server. No barrier, no intermediary, no commission.

## The mailing list as distribution channel

The mailing list is the most underrated direct distribution channel that exists. An email to your subscribers with a download link is distribution. No algorithm deciding whether they receive it. No platform taking a percentage. No data going to any third party.

Ethical mailing list tools:
- **Brevo** (formerly Sendinblue): free plan up to 300 emails/day. French company.
- **Mailchimp**: the most well-known, American, free up to 500 contacts.
- **Listmonk**: free software, self-hostable. Zero commissions, zero third-party data.

## Peertube for music videos

If you want to publish video clips or live recordings without YouTube, [Peertube](https://joinpeertube.org/) is the federated, free alternative. Like Funkwhale, you can join a community instance or host your own.

Peertube videos federate — someone on a different instance can follow and watch your videos without their own account.

## Practical summary

| Need | Free tool | Difficulty |
|---|---|---|
| Publish music with download | Faircamp (self-hosted) | Medium |
| Own federated streaming | Funkwhale (own instance or community) | Medium–high |
| Distribution by subscription | RSS feed from your website | Low |
| Direct music sales | Ko-fi + ZIP file | Low |
| Notify fans of new releases | Mailing list | Low |
| Videos without YouTube | Peertube | Medium |

## The truth about "without platforms"

Distributing music completely independently gives you total control and zero commissions. What it doesn't give you is passive discovery: no one will find you through algorithms because there aren't any. Your music will reach exactly the people you actively reach — not one fan more, not one fan less.

For artists who already have an established audience and a direct communication channel (mailing list, social media with real organic reach), independent distribution is perfectly viable. For artists still building their audience, platforms remain useful as discovery channels, even selectively.

The answer isn't one or the other: it's knowing which platform you use for discovery and which infrastructure you own for direct relationships with your audience.

**Read also:** [Who owns each music platform?](/en/resources/who-owns-music-platforms/) · [Bandcamp: first recommended complement](/en/resources/bandcamp-musicians-professional/) · [Distributing at concerts without CDs](/en/resources/selling-music-concerts-street-without-cd/)

At Ressona we help artists build their own infrastructure: website, domain, mailing list and distribution tools that don't depend on any third-party company. [Get in touch](/en/#contacte).
