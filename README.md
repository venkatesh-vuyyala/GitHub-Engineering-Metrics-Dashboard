# GitHub-Engineering-Metrics-Dashboard

## Overview
This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured Github Repository data based on the stars count, watchers, forks count and pull requests metrics.

## Project Goals

1. Data Ingestion — Build a mechanism to ingest data from different sources
2. ETL System — Getting data in raw format, transforming this data into the proper format
3. Data lake — Gathered data from multiple sources so we need centralized repo to store them
4. Scalability — As the size of our data increases, we need to make sure our system scales with it
5. Cloud — We can’t process vast amounts of data on our local computer so we need to use the cloud, in this case, we will use AWS
6. Reporting — Build a dashboard to get answers to the question asked earlier

## Services Used

1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
2. AWS IAM: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
3. QuickSight: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
5. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.
6. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.

## Dataset Used

The dataset comprises 2,917,951 GitHub repositories in (CSV) format, capturing key metrics such as repository names, star counts, forks, watchers, pull requests, primary languages, and languages used. It also includes the total number of commits, creation dates, and assigned licenses. This comprehensive dataset provides valuable insights into repository popularity, activity, and development practices across a wide range of programming languages and licensing models.
https://www.kaggle.com/datasets/nikhil25803/github-dataset

## Architecture Diagram
![architecture](https://github.com/user-attachments/assets/76431108-cf53-49f9-86e3-b1273db6a42a)

