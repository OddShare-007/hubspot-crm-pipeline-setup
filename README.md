# HubSpot CRM Pipeline Setup (Sample Project)

## Problem
Small e-commerce founders often track leads in messy sheets and lose deals because nothing is in one place. This sample project shows how I set up a clean CRM from scratch so leads, budgets and deal stages are easy to see and track.

## What I built
I set up a HubSpot CRM on the free plan and built a working sales pipeline for a sample store business. The free plan allows one deal pipeline with default stages, so I worked inside those limits and added custom data on top.

Custom contact properties I created: Lead Source (LinkedIn, Website, Referral, Instagram), Budget (number), Store Platform (Shopify, WooCommerce, Other).

I wrote a Python script with Faker to generate 30 sample contacts and 15 sample deals, then imported both files into HubSpot and mapped every column to the right property.

## Pipeline stages used
Appointment Scheduled, Qualified To Buy, Presentation Scheduled, Decision Maker Bought-In, Contract Sent, Closed Won, Closed Lost

## Tools used
HubSpot Free CRM, Python, Pandas, Faker, Google Colab, GitHub

## Screenshots

Deals board

Deals table with amount, stage and pipeline

Contacts list with custom properties

Custom properties list

## Result
30 contacts and 15 deals imported with zero skipped fields after fixing the column mapping. Every contact has a lead source, budget and store platform, so a founder can instantly see where leads come from and how much each deal is worth.

## Folder structure
data has the two CSV files, scripts has generate_data.py, screenshots has the images.

## Note
All names, emails and companies are fake and generated with Faker. This is a sample project, not client work.

## Author
Shubradeep Jana
Data Science student | CRM and Automation | Mumbai, India
