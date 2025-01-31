Architecting_On_AWS_07012025_Day2.md

Technical Essentials 2024 - Start Date: 7 January 2025 - [Unofficial Introduction to the course](./00-Personal_Taughts_07012025.pdf)

- [Network 2](#network-2)
- [Serverless](#serverless)

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

---
[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)

[TGW Examples, remember Regional and RAM](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html)

[TGW TGW Connect: Third Part Appliance](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)

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