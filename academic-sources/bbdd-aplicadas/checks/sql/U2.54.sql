-- u2 · Ejercicio U2.54: cómo está conectada la sesión actual.
SELECT
    net_transport AS Transporte,
    protocol_type AS Protocolo,
    auth_scheme   AS Autenticacion
FROM sys.dm_exec_connections
WHERE session_id = @@SPID;
