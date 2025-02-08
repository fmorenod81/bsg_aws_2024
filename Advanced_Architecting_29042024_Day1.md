Advanced_Architecting_29042024.md

Advanced Architecting on AWS 2024 - Start Date: 29 April 2024 - [Unofficial Introduction to the course](./00-Personal_Taughts_28042024.pdf)

AWS Blogs en Español - Link: [AWS Blogs](https://aws.amazon.com/es/blogs/aws-spanish/)

---

**Table of Contents**
- [The exam and the course](#the-exam-and-the-course)
- [Module 1: Review Architecting Concepts](#module-1-review-architecting-concepts)
- [Module 2: Single To Multiple Accounts](#module-2-single-to-multiple-accounts)
  - [Multiaccount strategies](#multiaccount-strategies)
  - [Identity Center](#identity-center)
  - [Control Tower](#control-tower)
- [Module 3: Hybrid Connectivity](#module-3-hybrid-connectivity)
  - [Client VPN](#client-vpn)
  - [Site-To-Site VPN](#site-to-site-vpn)
  - [Direct Connect](#direct-connect)
  - [Transit Gateway](#transit-gateway)
  - [Route 53 Private Resolver](#route-53-private-resolver)
- [Module 4: Specialized Infrastructure](#module-4-specialized-infrastructure)
  - [Storage Gateway](#storage-gateway)
  - [VmWare Cloud on AWS](#vmware-cloud-on-aws)
  - [Outposts](#outposts)
  - [Local Zones](#local-zones)
  - [Wavelength](#wavelength)
- [Module 5: Connecting Networks](#module-5-connecting-networks)
  - [Transit Gateway](#transit-gateway-1)
  - [Resource Access Manager](#resource-access-manager)
  - [PrivateLink](#privatelink)

---

## The exam and the course

AWS Solutions Architect Professional - Note Prerequisites - Link: [Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-sa-pro/AWS-Certified-Solutions-Architect-Professional_Exam-Guide.pdf)

Exam Prep: AWS Certified Solutions Architect - Professional - 5h - Link: [Digital Training](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14951/exam-prep-aws-certified-solutions-architect-professional-sap-c02)

Advanced Architecting on AWS - Link: [Course Outline](https://d1.awsstatic.com/training-and-certification/classroom-training/advanced-architecting-on-aws.pdf)

Advanced Architecting on AWS - Online Course Supplement - Link: [Digital Training](https://explore.skillbuilder.aws/learn/course/8319/play/75962/architecting-on-aws-online-course-supplement)

Advanced Architecting on AWS - Online Course Supplement - All Languages - Link: [Digital Training](https://www.aws.training/Details/eLearning?id=56205)

## Module 1: Review Architecting Concepts

Compare Options for VPC Endpoint for S3 - Link: [Official Blog](https://aws.amazon.com/blogs/architecture/choosing-your-vpc-endpoint-strategy-for-amazon-s3/)

## Module 2: Single To Multiple Accounts

Comparing AWS Deployment Tools to Manage Multiple Accounts - Link: [AWS re:Invent 2020 Video](https://youtu.be/n_6QTYDavrM)

Best Practices for Securing Your Multi-Account Environment  - Link: [AWS re:Invent 2020 Video](https://youtu.be/ip5sn3z5FNg)

Policy Evaluation: IAM, Permission Boundaries, SCP - Link: [Official Doc](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

### Multiaccount strategies

Cross-Account IAM Roles - Link: [Official Tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

Permissions Boundaries Exercise - Link: [AWS Live re:Inforce Video](https://www.youtube.com/watch?v=eVNvjQ0wr84)

Kahoot Answer 6 May - [PDF](./Kahoot_1_AA_06052024.pdf)

### Identity Center

AWS Organizations - Link: [Official FAQs](https://aws.amazon.com/organizations/faqs/)

Best Practices for AWS Organizations - Link: [Official Doc](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html)

Organizations Concepts - Link: [Official Doc](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)

Service Control Policies (SCP) Examples - Link: [Official Doc](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html)

AWS Services integrated with Organizations - Link: [Official Doc](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)

Identity Center - Link: [Official FAQs](https://aws.amazon.com/iam/identity-center/faqs/)

Understanding Key AWS Single Identity Center Concepts - Link: [Official Doc](https://docs.aws.amazon.com/singlesignon/latest/userguide/understanding-key-concepts.html)

How to create and manage users within AWS IAM Identity Center  - Link: [AWS Security Blog](https://aws.amazon.com/blogs/security/how-to-create-and-manage-users-within-aws-sso/)

Configure the AWS CLI to use IAM Identity Center token provider credentials with automatic authentication refresh  - Link: [Official Doc](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html)

### Control Tower

About controls in AWS Control Tower - Link: [Official Doc](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)

How AWS Control Tower Works - Link: [Official Doc](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html)

Best Practices for AWS Control Tower Administrators - Link: [Official Doc](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html)

Proactive Controls on Control Tower User Guide - Link: [Official Doc](https://docs.aws.amazon.com/controltower/latest/userguide/proactive-controls.html)

## Module 3: Hybrid Connectivity

Hybrid Connectivity - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.html)

MANDATORY!! Amazon Virtual Private Cloud Connectivity Options - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html)

### Client VPN

AWS Client VPN Administrator Guide - Link: [Official Doc](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

Accelerated Site-to-Site VPN Connections - Link: [Official Doc](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html)

ClientVPN Rules & Best Practices - Link: [Official Doc](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is-best-practices.html)

Client VPN Scenarios and examples - Link: [Official Doc](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/scenario.html)

NAT-Transversal - Link: [Wikipedia](https://en.wikipedia.org/wiki/NAT_traversal)

### Site-To-Site VPN

Site-to-Site VPN Tunnel Initiation Options - Link: [Official Doc](https://docs.aws.amazon.com/vpn/latest/s2svpn/initiate-vpn-tunnels.html)

Customer Gateway Options for Your Site-to-Site VPN Connection - Link: [Official Doc](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-options.html)

Improve VPN Network Performance of AWS Hybrid Cloud with Global Accelerator - Link: [Official Doc](https://aws.amazon.com/blogs/architecture/improve-vpn-network-performance-of-aws-hybrid-cloud-with-global-accelerator)

Site-to-Site VPN routing options - Link: [Official Doc](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNRoutingTypes.html)

### Direct Connect

FAQs: AWS Direct Connect: - Link: [Official FAQs](https://aws.amazon.com/directconnect/faqs/)

Hosted virtual interfaces on VIF - Note IP Requisites - Link: [Official Doc](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html#hosted-vif)

Traffic encription Options for DC - Link: [Official Doc](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/traffic-encryption-options-direct-connect-ra.pdf)

### Transit Gateway

Amazon Virtual Private Cloud Connectivity Options - Link: [Official Doc](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html)

Scaling VPN throughput using AWS Transit Gateway  - Link: [Official Doc](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/)

### Route 53 Private Resolver

Working with Private Hosted Zones - Link: [Official Doc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)

Resolving DNS Queries between VPCs and Your Network - Link: [Official Doc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)

Getting Started with Route 53 Resolver - Link: [Official Doc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html)

## Module 4: Specialized Infrastructure

Hybrid Cloud with AWS - Link: [Whitepaper](https://d1.awsstatic.com/whitepapers/hybrid-cloud-with-aws.pdf?did=wp_card&trk=wp_card)

**QUESTIONS**:

**a) What is the charge for having EC2 on Outposts?**

R:/ According to [AWS Questions on Repost](https://repost.aws/questions/QU5UM3emo5R4ypbOElxg4dQA/is-the-pricing-of-using-services-in-outpost-the-same-as-using-on-cloud) and [Outposts section on the How AWS Pricing Works Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-outposts.html); you have to pay for the service usage no for the capacity. On the repost, it appears the Load Balancer Example. To complement the pricing scheme, you can review [Outposts Pricing Guide](https://aws.amazon.com/outposts/rack/pricing/)

**b) What is the procedure of ASG on Outposts ?**

R:/I like this tech article about the capacity of [Load Balancer on Outposts](https://aws.amazon.com/blogs/networking-and-content-delivery/configuring-an-application-load-balancer-on-aws-outposts/)

### Storage Gateway

Tag: AWS File Gateway Tag on Blogs - Link: [AWS Storage Blog](https://aws.amazon.com/blogs/storage/tag/aws-file-gateway/)

AWS Storage Gateway - Link: [Official FAQs](https://aws.amazon.com/storagegateway/faqs/)

AWS Storage Gateway Primer: File Gateway - Link: [Official Training](https://www.aws.training/Details/Curriculum?id=38145)

Deep Dive into AWS Storage Gateway - Link: [Official Training](https://www.aws.training/Details/Curriculum?id=19403)

### VmWare Cloud on AWS

VMware Cloud on AWS - Link: [Official FAQs](https://aws.amazon.com/vmware/faqs/)

Enabling Business Continuity with VMware Cloud on AWS - Link: [AWS re:Invent 2020](https://youtu.be/w2mD0Z5eh6o)

Migrate and Modernize with VMware Cloud on AWS - Link: [AWS re:Invent 2020](https://youtu.be/FQ_u9KsyQyE)

### Outposts

AWS Outposts: Storage Foundations - Amazon S3 on Outposts - Link: [AWS Online Tech Talks](https://youtu.be/A_khazmf6jU)

### Local Zones

Delivering low-latency applications at the edge - Link: [AWS re:Invent 2030 Video](https://www.youtube.com/watch?v=isYOTxCm5w4)

### Wavelength

Telecom Reference for AWS - Link: [Official Page](https://aws.amazon.com/telecom/resources/)

At the cutting edge: AI driven sustainable 5G networks - Link: [AWS re:Invent 2023 Video](https://www.youtube.com/watch?v=uG70n3vJLzc)

AWS Wavelength: Run Apps with Ultra-Low Latency at 5G Edge - Link: [AWS re:Invent 2020 Video](https://youtu.be/AQ-GbAFDvpM)

Architecting 5G Apps for Ultra-Low Latency on AWS Wavelength - Link: [AWS re:Invent 2020 Video](https://youtu.be/KZX5FcsDfUQ)

## Module 5: Connecting Networks

 MANDATORY!! Building a Scalable and Secure Multi-VPC AWS Network Infrastructure - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/building-scalable-secure-multi-vpc-network-infrastructure.pdf)

### Transit Gateway

FAQs: AWS Transit Gateway - Link: [Official FAQs](https://aws.amazon.com/transit-gateway/faqs/)

Transit Gateway Guide: Examples - Link: [Official Doc](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html)

Field Notes: Working with Route Tables in AWS Transit Gateway - Link: [Architecture Blog](https://aws.amazon.com/blogs/architecture/field-notes-working-with-route-tables-in-aws-transit-gateway/)

Advanced Architectures with AWS Transit Gateway - Link: [AWS Online Tech Talks](https://youtu.be/awrdICiS6ug)

Transit Gateway Networking and Scaling - Link: [Training](https://www.aws.training/Details/eLearning?id=40275)

### Resource Access Manager

FAQs: AWS Resource Access Manager - Link: [Official FAQs](https://aws.amazon.com/ram/faqs/)

Sharing Your AWS Resources - Link: [Official Doc](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html)

Shareable AWS Resources - Link: [Official Doc](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html)

### PrivateLink

Integrating AWS Transit Gateway with AWS PrivateLink and Amazon Route 53 Resolver - Link: [BigData Blog](https://aws.amazon.com/blogs/big-data/how-goldman-sachs-builds-cross-account-connectivity-to-their-amazon-msk-clusters-with-aws-privatelink/)

Configure and Deploy AWS PrivateLink - Link: [Training](https://www.aws.training/Details/eLearning?id=54077)

Learn About Private Endpoints in Atlas (AWS Partner Solution)- Link: [Official Doc](https://www.mongodb.com/docs/atlas/security-private-endpoint/)

VPC Endpoint Services for Interface Endpoints - Link: [Official Doc](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service-overview.html)
