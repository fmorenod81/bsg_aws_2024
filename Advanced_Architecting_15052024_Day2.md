Advanced_Architecting_15052024.md

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

### Deployment Models

Blue/Green Deployment with CodeDeploy - Link: [Official Doc](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html)

Fine-Tuning Blue/Green Deployments on Application Load Balancer- Link: [Official Doc](https://aws.amazon.com/blogs/devops/blue-green-deployments-with-application-load-balancer/)

Understanding How Deployments Affect Application Performance- Link: [AWS re:Invent 2020 Video](https://youtu.be/O9tDtJje-EA)

### AWS Cloudformation Stacksets

Working with AWS CloudFormation StackSets - Link: [Official Doc](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

Prerequisites for stack set operations on "Self-Managed" and "Trusted Access" - Link: [Official Doc](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html)

## Module 8: High Availability and DDoS

AWS Best Practices for DDoS Resiliency - Link: [Whitepaper](https://d0.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf)

Protect Your Web-Facing Workloads with AWS Security Services - Link: [Training](https://www.aws.training/Details/Video?id=27496)

### AWS WAF

FAQs: AWS WAF - Link: [Official FAQs](https://aws.amazon.com/waf/faq/)

Using AWS WAF and AWS Secrets Manager to Enforce Amazon CloudFront Origins - Link: [AWS re:Invent 2020 Video](https://youtu.be/32jU3lVumAk)

### AWS Shield Advanced

FAQs: AWS Shield - Link: [Official FAQs](https://aws.amazon.com/shield/faqs/)

How AWS Shield Works - Link: [Official Doc](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)

### AWS Firewall Manager

FAQs: AWS Firewall Manager - Link: [Official FAQs](https://aws.amazon.com/firewall-manager/faqs/)

AWS Firewall Manager Now Supports Security Groups on Application Load Balancers and Classic Load Balancers - Link: [Official News](https://aws.amazon.com/about-aws/whats-new/2020/08/aws-firewall-manager-now-supports-security-groups-on-albs-and-elbs/)

Centrally Manage AWS WAF and AWS Managed Rules Using AWS Firewall Manager - Link: [AWS Online Tech Talks](https://youtu.be/u27HLad-Wi8)

### AWS Network Firewall

Introducing AWS Gateway Load Balancer - Link: [Official News](https://aws.amazon.com/about-aws/whats-new/2020/11/introducing-aws-gateway-load-balancer/)

FAQs: AWS Network Firewall - Link: [Official FAQs](https://aws.amazon.com/network-firewall/faqs/)

Introducing AWS Network Firewall- Link: [AWS re:Invent 2020 Video](https://youtu.be/CISgqpVn75Q)

## Module 9: Securing Data

### Cryptography

### AWS KMS

### AWS Cloud HSM

### AWS Secret Manager

## Module 10: Large Scale Data Stores

### S3 Data Management

### Data Lakes

### AWS Lake Formation
