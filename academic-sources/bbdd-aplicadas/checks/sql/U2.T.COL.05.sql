-- u2 · Collation: página de códigos de una intercalación con y sin UTF-8 (SQL Server 2019 o posterior).
SELECT
    'Latin1_General_CI_AS'               AS Intercalacion,
    COLLATIONPROPERTY('Latin1_General_CI_AS', 'CodePage') AS PaginaDeCodigos
UNION ALL
SELECT
    'Latin1_General_100_CI_AS_SC_UTF8',
    COLLATIONPROPERTY('Latin1_General_100_CI_AS_SC_UTF8', 'CodePage');
