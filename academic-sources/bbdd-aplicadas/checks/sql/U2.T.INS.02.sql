-- u2 · Instalación: instancia, modo de autenticación y cómo está conectada la sesión actual.
SELECT
    CASE WHEN SERVERPROPERTY('InstanceName') IS NULL THEN 'predeterminada' ELSE 'con nombre' END AS Instancia,
    CASE SERVERPROPERTY('IsIntegratedSecurityOnly') WHEN 1 THEN 'solo Windows' ELSE 'mixto' END AS Autenticacion,
    c.net_transport    AS Transporte,
    c.local_tcp_port   AS Puerto
FROM sys.dm_exec_connections AS c
WHERE c.session_id = @@SPID;
