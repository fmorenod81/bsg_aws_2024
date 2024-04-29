Advanced_Architecting_29042024.md

Advanced Architecting on AWS 2024 - Start Date: 29 April 2024 - [Unofficial Introduction to the course](./00-Personal_Taughts_28042024.pdf)

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

### Multiaccount strategies

AWS Organizations - Link: [Official FAQs](https://aws.amazon.com/organizations/faqs/)

Best Practices for AWS Organizations - Link: [Official Doc](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html)

Organizations Concepts - Link: [Official Doc](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)

Cross-Account IAM Roles - Link: [Official Tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

### Identity Center

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

MANDATORY!! Amazon Virtual Private Cloud Connectivity Options- Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html)

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

### Transit Gateway

Amazon Virtual Private Cloud Connectivity Options - Link: [Official Doc](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html)

Scaling VPN throughput using AWS Transit Gateway  - Link: [Official Doc](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/)

### Route 53 Private Resolver

Working with Private Hosted Zones - Link: [Official Doc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)

Resolving DNS Queries between VPCs and Your Network - Link: [Official Doc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)

Getting Started with Route 53 Resolver:  - Link: [Official Doc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html)

