:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_LOG_05';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
INSERT dbo.Pedido (Estado) VALUES ('base');
BEGIN TRANSACTION Confirmada;
INSERT dbo.Pedido (Estado) VALUES ('se confirma');
COMMIT TRANSACTION Confirmada;
BEGIN TRANSACTION Revertida;
INSERT dbo.Pedido (Estado) VALUES ('se revierte');
ROLLBACK TRANSACTION Revertida;
GO
:out stdout
SELECT t.Transaccion, t.Registro, t.Operaciones
FROM (
    SELECT b.[Transaction Name] AS Transaccion, o.Operation AS Registro, COUNT(*) AS Operaciones
    FROM sys.fn_dblog(NULL, NULL) AS b
    JOIN sys.fn_dblog(NULL, NULL) AS o ON o.[Transaction ID] = b.[Transaction ID]
    WHERE b.Operation = 'LOP_BEGIN_XACT' AND b.[Transaction Name] IN ('Confirmada', 'Revertida')
      AND o.Operation IN ('LOP_COMMIT_XACT', 'LOP_ABORT_XACT', 'LOP_INSERT_ROWS', 'LOP_DELETE_ROWS')
    GROUP BY b.[Transaction Name], o.Operation
) AS t
ORDER BY t.Transaccion, t.Registro;
