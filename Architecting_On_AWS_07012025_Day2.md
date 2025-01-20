Architecting_On_AWS_07012025_Day2.md

Technical Essentials 2024 - Start Date: 7 January 2025 - [Unofficial Introduction to the course](./00-Personal_Taughts_07012025.pdf)

- [Storage](#storage)

## Storage

[Redundancia 3 zonas](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)

[s3](https://aws.amazon.com/s3/features/)

[Proteccion/Permisos](https://aws.amazon.com/s3/faqs/?nc=sn&loc=7#Security)

[Tiene endpoint publico para acceso, no significa que sea publico. Publico: Bucket Policies (Para hacerlo publico), ACL y CORS - Cross-Origin Resource Sharing](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/)

[Ownership Grafico](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

[Access Point - Solo para objetos](https://aws.amazon.com/s3/features/access-points/)

[Dividir centralizacion en Bucket Policies](https://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/)

[Por Network Control Origin (VPC), Usuario, Grupo, Cross-Account](https://aws.amazon.com/s3/faqs/?nc=sn&loc=7#S3_Access_Points)

[Alineado con SCP y con politicas de bucket - Ejemplos](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html)

[Enc at rest - Default enc x Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)

[SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html)

[DSSE-KMS-$$-New13Jun2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-s3-dual-layer-encryption-compliance-workloads/)

[Object Lock - WORM (Retention Period- No Del, No Updates & Legal Hold) - Aplica al crearse](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html)

[Lifecycle - Basados en Creacion pero puede aplicar otros filtros, tamaño. Ejemplo 6.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lifecycle-config-conceptual-ex6)

[Replicacion](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html)

[Transfer Acceleration - PUT/GET](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-speed-comparison.html)

[Another sh Tool](https://repost.aws/knowledge-center/upload-speed-s3-transfer-acceleration)

[Integracion con EventBridge - Cap. 7 ](https://aws.amazon.com/blogs/aws/new-use-amazon-s3-event-notifications-with-amazon-eventbridge/)
