-- u5 · log-recuperacion: transacciones abiertas (código de la página) con una transacción propia abierta.
CREATE TABLE dbo.Movimiento (MovimientoId INT PRIMARY KEY, Importe INT);
BEGIN TRANSACTION Pendiente;
INSERT dbo.Movimiento VALUES (1, 100);
CREATE TABLE #OpenTran (Campo NVARCHAR(128), Valor NVARCHAR(256));
INSERT #OpenTran EXEC (N'DBCC OPENTRAN WITH TABLERESULTS, NO_INFOMSGS');
SELECT Valor AS TransaccionMasAntigua FROM #OpenTran WHERE Campo = N'OLDACT_NAME';
CREATE TABLE #Abierta (transaction_id BIGINT, name NVARCHAR(32), transaction_begin_time DATETIME, session_id INT);
INSERT #Abierta
SELECT at.transaction_id,
       at.name,
       at.transaction_begin_time,
       st.session_id
FROM sys.dm_tran_active_transactions AS at
LEFT JOIN sys.dm_tran_session_transactions AS st
  ON st.transaction_id = at.transaction_id;
SELECT name AS Transaccion, IIF(session_id = @@SPID, 'esta sesión', 'otra') AS Sesion
FROM #Abierta
WHERE name = N'Pendiente';
ROLLBACK;
