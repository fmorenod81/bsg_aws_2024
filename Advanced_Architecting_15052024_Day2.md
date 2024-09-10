Advanced_Architecting_15052024.md

AWS Blogs en Español - Link: [AWS Blogs](https://aws.amazon.com/es/blogs/aws-spanish/)

---

**Table of Contents**
- [Module 6: Containers](#module-6-containers)
  - [Containers](#containers)
  - [Containers hosting on AWS](#containers-hosting-on-aws)
  - [Amazon ECS](#amazon-ecs)
  - [Amazon EKS](#amazon-eks)
- [Module 7: Continuous Integration/Continuous Delivery (CI/CD)](#module-7-continuous-integrationcontinuous-delivery-cicd)
  - [CI/CD](#cicd)
  - [Code Services](#code-services)
  - [Deployment Models](#deployment-models)
  - [AWS Cloudformation Stacksets](#aws-cloudformation-stacksets)
- [Module 8: High Availability and DDoS](#module-8-high-availability-and-ddos)
  - [AWS WAF](#aws-waf)
  - [AWS Shield Advanced](#aws-shield-advanced)
  - [AWS Firewall Manager](#aws-firewall-manager)
  - [AWS Network Firewall](#aws-network-firewall)
- [Module 9: Securing Data](#module-9-securing-data)
  - [Cryptography](#cryptography)
  - [AWS KMS](#aws-kms)
  - [AWS Cloud HSM](#aws-cloud-hsm)
  - [AWS Secret Manager](#aws-secret-manager)
- [Module 10: Large Scale Data Stores](#module-10-large-scale-data-stores)
  - [S3 Data Management](#s3-data-management)
  - [Data Lakes](#data-lakes)
  - [AWS Lake Formation](#aws-lake-formation)

---

## Module 6: Containers

**QUESTIONS**:

**a) What is Capacity Provider on ECS?**

R:/ According to Amazon Q:
Capacity Providers in Amazon ECS (Elastic Container Service) are a feature that allows you to define the compute capacity that your ECS tasks can run on. Here's a summary of how Capacity Providers work:

- **Fargate Capacity Providers:** When using Fargate, the Fargate and Fargate Spot capacity providers are automatically available. You can associate these capacity providers with your ECS cluster to distribute tasks between Fargate on-demand and Fargate Spot instances.

- **EC2 Capacity Providers:** When using EC2 instances, you can create custom capacity providers that are backed by Auto Scaling groups. This allows you to mix different instance types, on-demand and spot instances, and define strategies to distribute tasks among them.

- **Task Distribution:** Capacity providers help you distribute tasks across different compute options. For example, you can define a strategy to run 50% of tasks on Fargate on-demand and 50% on Fargate Spot.

- **Autoscaling Integration:** Capacity providers can be integrated with Auto Scaling groups to enable Cluster Auto Scaling (CAS). This allows ECS to automatically scale the underlying EC2 capacity based on the number of pending tasks.

- **Managed Scaling and Draining:** Capacity providers offer features like managed scale-in protection and managed draining to ensure graceful handling of instance termination and task migrations.

- **Troubleshooting:** If you encounter scaling issues with your capacity providers, you can check factors like service association, scaling policy configuration, task placement strategy, and Auto Scaling group issues.

For the most up-to-date information on Capacity Providers, pricing, limits, and other details, please refer to the [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity-provider-console-v2.html).


**a) What is EKS Anywhere?**
R:/ I have to correct myself, because I thought it was a Kubernetes operator for multicloud and hybrid environments; however it applies for hybrid environments ONLY, when you have on-premises resources and you like to manage using AWS Console. More information about [Amazon EKS Anywhere](https://aws.amazon.com/es/eks/eks-anywhere/)

### Containers

Docker Guides - Link: [Docker Page](https://docs.docker.com/get-started/overview/)

Docker Engine overview - Link: [Docker Page](https://docs.docker.com/engine/)

Understanding Docker Container Architecture - Link: [No-Official Blog](https://collabnix.com/understanding-docker-container-image/)

Docker Tag  - Link: [Docker Page](https://docs.docker.com/engine/reference/commandline/tag/)

Deep Dive on Container Security - Link: [Training](https://www.aws.training/Details/Video?id=26841)

### Containers hosting on AWS

Containers on AWS: An Introduction - Link: [AWS Public Sector Summit Video](https://www.youtube.com/watch?v=kBi-s3eV2Ec)

Build and Deploy Straight from Docker to AWS - Link: [AWS Cloud Containers Conference](https://youtu.be/V88Iqdm8GkE)

FAQs: Amazon Elastic Container Registry - Link: [Official FAQs](https://aws.amazon.com/ecr/faqs/)

FAQs: AWS Fargate - Link: [Official FAQs](https://aws.amazon.com/fargate/faqs/)

AWS Fargate: Are Serverless Containers Right for You? - Link: [AWS re:Invent 2020 Video](https://youtu.be/Vtymod0nPBo)

Deep Dive on AWS Fargate: Building Serverless Containers at Scale - Link: [Training](https://www.aws.training/Details/Video?id=26855)

### Amazon ECS

FAQs: Amazon Elastic Container Service - Link: [Official FAQs](https://aws.amazon.com/ecs/faqs/)

Getting Up and Running with Amazon ECS - Link: [AWS re:Invent 2020 Video](https://youtu.be/9u_HKS_Lv6o)

Amazon Elastic Container Service (ECS) Primer - Link: [Training](https://www.aws.training/Details/eLearning?id=30260)

ECS Task Execution roles at Computing Host (ECS Agent) Level - Link: [Official Doc](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html)

ECS Task role at Container (Task) Level - Link: [Official Doc](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)

ECS Workshop, section of Capacity Provider - Link: [ECS Workshop](https://ecsworkshop.com/capacity_providers/capacityprovider_primer/)

### Amazon EKS

FAQs: Amazon EKS - Link: [Official FAQs](https://aws.amazon.com/eks/faqs/)

Amazon EKS on AWS Fargate Deep Dive - Link: [AWS re:Invent 2020 Video](https://youtu.be/9tQFXEhHdn0)

Amazon EKS and AWS Fargate: Better Together - Link: [AWS Container Day](https://www.youtube.com/watch?v=-xMNbys0tF8)

Amazon Elastic Kubernetes Service (EKS) Primer - Link: [Training](https://www.aws.training/Details/eLearning?id=32894)

Introducing Amazon EKS Distro (EKS-D) - Link: [AWS Blog](https://aws.amazon.com/blogs/opensource/introducing-amazon-eks-distro/)

## Module 7: Continuous Integration/Continuous Delivery (CI/CD)

Whitepaper: Introduction to DevOps on AWS - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/introduction-devops-aws.pdf)

### CI/CD

Thinking Serverless: From Business Problem to Serverless Solution - Link: [AWS re:Invent 2020 Video](https://youtu.be/Z57KLdJZnGA)

Infrastructure as Code on AWS - Link: [AWS Online Tech Talks](https://youtu.be/cKQtPZwf97s)

Getting Started with DevOps on AWS - Link: [Training](https://www.aws.training/Details/Curriculum?id=67465)

AWS Cloud Development Kit Primer - Link: [Training](https://www.aws.training/Details/Curriculum?id=64511)

### Code Services

Hands-Off: Automating Continuous Delivery Pipelines at Amazon - Link: [AWS re:Invent 2020 Video](https://youtu.be/ngnMj1zbMPY)

AWS CodePipeline product integrations - Link: [Official Webpage](https://aws.amazon.com/codepipeline/product-integrations/)

AWS CodeDeploy Integrations - Link: [Official Webpage](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations.html)

Build specification reference for CodeBuild (buildspec.yaml) - Link: [Official Docs](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)

CodeDeploy AppSpec file reference (AppSpec .yaml) - Link: [Official Docs](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html)

### Deployment Models

Blue/Green Deployment with CodeDeploy - Link: [Official Doc](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html)

Fine-Tuning Blue/Green Deployments on Application Load Balancer- Link: [Official Doc](https://aws.amazon.com/blogs/devops/blue-green-deployments-with-application-load-balancer/)

Understanding How Deployments Affect Application Performance- Link: [AWS re:Invent 2020 Video](https://youtu.be/O9tDtJje-EA)

### AWS Cloudformation Stacksets

Working with AWS CloudFormation StackSets - Link: [Official Doc](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

Prerequisites for stack set operations on "Self-Managed" and "Trusted Access" - Link: [Official Doc](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html)

## Module 8: High Availability and DDoS

**QUESTIONS**:

**a) Are there any pricing difference between Global WAF deployment (for Cloudfront) and Regional WAF Deployment (ELB, API Gateway and others) ?**

R:/ No, according to [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/), it says: "You will be charged for each web ACL that you create and each rule that you create per web ACL". Therefore, you are charging by ACL, rules and rule type (Bot Control and Fraud control), please check the page to have a better perspective.

**a) What are the coverage of Firewall Manager ? Includes Network Firewall?**

R:/ Yes, it includes Network Firewall and others like: AWS WAF rules, AWS Shield Advanced protections, VPC security groups, VPC network access control lists (ACLs) and Amazon Route 53 Resolver DNS Firewall rules across multiple AWS accounts and resources from a single place. More info at [AWS Firewall Manager FAQs](https://aws.amazon.com/firewall-manager/faqs/)


--

AWS Best Practices for DDoS Resiliency - Link: [Whitepaper](https://d0.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf)

Protect Your Web-Facing Workloads with AWS Security Services - Link: [Training](https://www.aws.training/Details/Video?id=27496)

### AWS WAF

FAQs: AWS WAF - Link: [Official FAQs](https://aws.amazon.com/waf/faq/)

Using AWS WAF and AWS Secrets Manager to Enforce Amazon CloudFront Origins - Link: [AWS re:Invent 2020 Video](https://youtu.be/32jU3lVumAk)

Deploy a dashboard for AWS WAF with minimal effort - Link: [AWS Security Blog](https://aws.amazon.com/blogs/security/deploy-dashboard-for-aws-waf-minimal-effort/)

AWS WAF Workshop - Link: [No-Official Workshop for Classic WAF](https://github.com/toshke/aws-waf-demo-workshop/tree/master)

Security Automations for AWS WAF - Link: [AWS Page](https://aws.amazon.com/solutions/implementations/aws-waf-security-automations/)

Jump to a Console - Link: [AWS WAF Console](https://us-east-1.console.aws.amazon.com/wafv2/homev2/web-acls/new?region=us-east-2)

### AWS Shield Advanced

FAQs: AWS Shield - Link: [Official FAQs](https://aws.amazon.com/shield/faqs/)

How AWS Shield Works - Link: [Official Doc](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)

### AWS Firewall Manager

AWS Firewall Manager prerequisites - Link: [Official Docs](https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html)

FAQs: AWS Firewall Manager - Link: [Official FAQs](https://aws.amazon.com/firewall-manager/faqs/)

AWS Firewall Manager Now Supports Security Groups on Application Load Balancers and Classic Load Balancers - Link: [Official News](https://aws.amazon.com/about-aws/whats-new/2020/08/aws-firewall-manager-now-supports-security-groups-on-albs-and-elbs/)

Centrally Manage AWS WAF and AWS Managed Rules Using AWS Firewall Manager - Link: [AWS Online Tech Talks](https://youtu.be/u27HLad-Wi8)

### AWS Network Firewall

Introducing AWS Gateway Load Balancer - Link: [Official News](https://aws.amazon.com/about-aws/whats-new/2020/11/introducing-aws-gateway-load-balancer/)

FAQs: AWS Network Firewall - Link: [Official FAQs](https://aws.amazon.com/network-firewall/faqs/)

Introducing AWS Network Firewall - Link: [AWS re:Invent 2020 Video](https://youtu.be/CISgqpVn75Q)

## Module 9: Securing Data

### Cryptography

Architecting for Database Encryption on AWS - Link: [AWS Blog](https://aws.amazon.com/blogs/security/architecting-for-database-encryption-on-aws/)

### AWS KMS

FAQs: AWS Key Management Service - Link: [Official FAQs](https://aws.amazon.com/kms/faqs/)

Using server-side encryption with customer-provided keys (SSE-C) - Link: [Official Doc](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html#sse-c-highlights)

### AWS Cloud HSM

FAQs: AWS CloudHSM - Link: [Official FAQs](https://aws.amazon.com/cloudhsm/faqs/)

### AWS Secret Manager

FAQ: AWS Secrets Manager - Link: [Official FAQs](https://aws.amazon.com/secrets-manager/faqs/)

Key Terms and Concepts for AWS Secrets Manager - Link: [Official Doc](https://docs.aws.amazon.com/secretsmanager/latest/userguide/terms-concepts.html)

## Module 10: Large Scale Data Stores

Managing Amazon Simple Storage Service (Amazon S3) - Link: [Training](https://www.aws.training/Details/Curriculum?id=66254)

Deep Dive into Amazon Simple Storage Service (Amazon S3) - Link: [Training](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/497/amazon-simple-storage-service-amazon-s3-storage-classes-deep-dive)

 Auditing Amazon Simple Storage Service (Amazon S3) Security - Link: [Training](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/502/auditing-amazon-simple-storage-service-amazon-s3-security)

### S3 Data Management

FAQs: Amazon S3 - Link: [Official FAQs](https://aws.amazon.com/s3/faqs/)

Amazon S3 Update – Strong Read-After-Write Consistency - Link: [AWS Blog](https://aws.amazon.com/blogs/aws/amazon-s3-update-strong-read-after-write-consistency/) and [Consistency Page](https://aws.amazon.com/s3/consistency/)

Managing data access with Amazon S3 access points - Link: [AWS Blog](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)

Configuring Amazon S3 security settings and access controls - Link: [AWS Re:Invent 2023 PDF](https://d1.awsstatic.com/events/Summits/reinvent2023/STG317-R_Configuring-Amazon-S3-security-settings-and-access-controls-REPEAT.pdf)

Setting Up Cross-Account Amazon S3 Access with S3 Access Points - Link: [AWS Blog](https://aws.amazon.com/blogs/storage/setting-up-cross-account-amazon-s3-access-with-s3-access-points/?nc1=b_rp)

Architecting for High Availability on Amazon S3 - Link: [AWS re:Invent 2020 Video](https://youtu.be/Qib1snR9FhA)

S3 Access Point Demo - Link: [No-Official Video](https://www.youtube.com/watch?v=iqCmDLMT4qU&t=463s)

### Data Lakes

Introduction to Designing Data Lakes on AWS - Link: [Coursera Course](https://www.coursera.org/learn/introduction-to-designing-data-lakes-in-aws?)

### AWS Lake Formation

FAQs: AWS Lake Formation - Link: [Official FAQs](https://aws.amazon.com/lake-formation/faqs/)

Cross Account Catalog Access Using Amazon Athena and AWS Lake Formation - Link: [AWS re:Invent 2020 Video](https://youtu.be/He8GvOFdjnE)