Architecting_On_AWS_01042025_Day3.md

Architecting_On_AWS_01042025_Day1.md - [Unofficial Introduction to the course](./00-Personal_Taughts_01042025.pdf)


- [Network 2](#network-2)
- [Serverless](#serverless)
- [Edge](#edge)
- [Backup and Recovery](#backup-and-recovery)
- [Course Summary](#course-summary)

## Network 2

[Hybrid Connection Options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html)

[Reliability Options](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/reliability.html)

---

[No cover on course: GW VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)

[No cover on course: GW VPC Endpoint/Target on your Routing Table - Acepta ambas-Comparison](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html#types-of-vpc-endpoints-for-s3)

[Interface VPC Endpoint / ENI Private IP in your VPC - Powered by PrivateLink - NetLB and ENI no managed by customer](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/how-does-aws-privatelink-work.html)

[Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html)

[Interface VPC Endpoint / ENI Private IP in your VPC - Pricing x hr y x trafico](https://aws.amazon.com/privatelink/pricing/#Interface_Endpoint_pricing)

[Interface VPC Endpoint / ENI Private IP in your VPC-Selecciona Subnets, 1 x AZ. Resolucion DNS](https://repost.aws/knowledge-center/vpc-interface-configure-dns)

[AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html)

[No cover on course:GW LB Endpoint](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html)

[No cover on course: SkillBuilder: Module 10: Networking 2: GW Load Balanced Endpoints](https://explore.skillbuilder.aws/learn/course/external/view/elearning/8319/architecting-on-aws-online-course-supplement)

---

[VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html)

[Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html)

[Data Transfer: Intra-region? Inter-region? ](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/)

---

[What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

[VPN Site2Site - 2 Tunnels on different AZ](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html)

[PreReqs, VPGW, Customer GW, RT, SecGroups, VPN Connection (here is the enc), Download CusGW y apply-Steps](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html)

[Pricing](http://calculator.aws)

[DxC Redundancy](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-redundant-connection.html)

[DxC New Locations](https://aws.amazon.com/directconnect/features/?nc=sn&loc=2&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc#What.27s_new_with_AWS_Direct_Connect)

[DxC on Queretero, 25-Jan-2025](https://aws.amazon.com/about-aws/whats-new/2025/01/aws-direct-connect-expansion-queretaro-mexico/)

[DxC Partnerships on LATAM](https://aws.amazon.com/directconnect/partners/?nc=sn&loc=7&dn=1)

---
[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)

[TGW Examples, remember Regional and RAM](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html)

[TGW TGW Connect: Third Part Appliance](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)

[How to use AWS Network Manager to visualize Transit Gateways across multiple accounts in the AWS Organization](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-use-aws-network-manager-to-visualize-transit-gateways-across-all-accounts-in-the-aws-organization/)

## Serverless

[AWS Serverless](https://aws.amazon.com/serverless/)

[API GW: AuthN&AuthZ: API Keys & OAuth/JWT-Lambda Authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)

[API GW: Brazilian Bank](https://github.com/aws-samples/openbanking-brazilian-auth-samples)

[GraphQL](https://aws.amazon.com/graphql/serverless-api/)

---

[Building Loosely Coupled, Scalable, C# Applications with Amazon SQS and Amazon SNS](https://aws.amazon.com/blogs/compute/building-loosely-coupled-scalable-c-applications-with-amazon-sqs-and-amazon-sns/)

[Loosely Coupled Scenarios](https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/loosely-coupled-scenarios.html)

[Amazon SQS standard queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html)

[Amazon SQS FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html)

[SQS FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html)

[SQS Short vs Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html#sqs-short-polling)

---

[SNS Retries](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html)

---

[Amazon Kinesis](https://aws.amazon.com/kinesis/)

[What is Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

[Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html)

[Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink/)

---

[Step Functions Concepts](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-states.html)

[Integrating services with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/integrate-services.html)

[Discovering workflow states to use in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-states.html)

[Amazon States Language](https://states-language.net/spec.html)


*QUESTIONS :*

*Q: Cual es la opcion de Dead-Letter para el Servicio SNS ?*

R:/ Es una cola de SQS que recibe las notificaciones que no se pueden recibir. La documentacion de la Cola de SQS en SNS esta [aqui](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html). Y la misma opcion en SQS esta [aqui](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).

*Q: Cuales pueden ser los casos de uso de Kinesis Video Streams ?*

R:/En la pagina oficial, estan los [casos de uso](https://aws.amazon.com/kinesis/video-streams/?nc=sn&loc=2&dn=1&amazon-kinesis-video-streams-resources-blog.sort-by=item.additionalFields.createdDate&amazon-kinesis-video-streams-resources-blog.sort-order=desc)

## Edge

---

[Monitoring health checks using CloudWatch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-checks.html)

[Working with hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html)

[Usage Cases using Route 53 Resolver: OnPrem](https://aws.amazon.com/blogs/security/simplify-dns-management-in-a-multiaccount-environment-with-route-53-resolver/)

[Choosing a routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)

[How do I configure geoproximity routing using the Route 53 console?](https://youtu.be/zxSDRPQRd50?t=158)

---

[Cloudfront How is work?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html)

[Cloudfront Sec: OAC Origina Access Control to access S3/Aug 22](https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-cloudfront-origin-access-control/)

[Cloudfront Sec:](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)

[Cloudfront Cache Configuration: Static Assets](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)

[Cloudfront Configuration: Dynamic Content](https://aws.amazon.com/cloudfront/dynamic-content/)

[Cloudfront Configuration: Cache Policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html)

[Using Amazon CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)

[MI PROPIA CUENTA: WAF Console](https://us-east-1.console.aws.amazon.com/wafv2/homev2/web-acls/new?region=us-east-1)

---

[UDP reflection attacks](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/udp-reflection-attacks.html)

[How AWS Shield and Shield Advanced work](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)

[AWS Shield Advanced pricing](https://aws.amazon.com/shield/pricing/)

[Setting up AWS WAF and its components](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)

[Using rule statements in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements.html)

[Use AWS Firewall Manager to deploy protection at scale in AWS Organizations](https://aws.amazon.com/blogs/security/use-aws-firewall-manager-to-deploy-protection-at-scale-in-aws-organizations/)

[Centrally manage AWS WAF (API v2) and AWS Managed Rules at scale with Firewall Manager](https://aws.amazon.com/blogs/security/centrally-manage-aws-waf-api-v2-and-aws-managed-rules-at-scale-with-firewall-manager/)

[AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/welcome.html)

---

[Site requirements for Outposts racks](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html)

[AWS resources on Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html#services)

[Connecting AWS Outposts to on-premises data sources](https://aws.amazon.com/blogs/storage/connecting-aws-outposts-to-on-premises-data-sources/)

## Backup and Recovery

[AWS Backup](https://aws.amazon.com/blogs/aws/aws-backup-automate-and-centrally-manage-your-backups/)

[AWS Backup: Supported AWS Resources and Applications](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#supported-resources)

[AWS Backup – Automate and Centrally Manage Your Backups](https://aws.amazon.com/blogs/aws/aws-backup-automate-and-centrally-manage-your-backups/)

[Monitoring AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.htm)

[Managing AWS Backup Resources Across Multiple AWS Accounts](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)

[Creating a Backup Plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)

[Disaster Recovery (DR) Architecture on AWS, Part III: Pilot Light and Warm Standby](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/)

[Disaster Recovery (DR) Architecture on AWS, Part IV: Multi-Site Active/Active](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iv-multi-site-active-active/)

## Course Summary

[Certification Preparation](https://aws.amazon.com/certification/certification-prep)

[Prepare for Examen](https://skillbuilder.aws/#prepare-for-exam)

[Certification Preparation - Testing](https://aws.amazon.com/certification/certification-prep/testing/)

[Digital Training](https://aws.amazon.com/training/digital)

[Digital training](https://explore.skillbuilder.aws/)

[Classroom training](https://aws.amazon.com/training)

[AWS Certification](https://aws.amazon.com/certification)

[AWS Workshops](https://workshops.aws/)

[Tech Talks](https://aws.amazon.com/events/online-tech-talks/on-demand/)

[AWS Ramp-Up Guides](https://aws.amazon.com/training/ramp-up-guides/)
