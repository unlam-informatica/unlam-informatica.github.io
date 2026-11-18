-- u1 · repaso: PK nonclustered y clustered en otra columna.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Movimiento (
    MovimientoId INT           NOT NULL CONSTRAINT PK_Movimiento PRIMARY KEY NONCLUSTERED,
    Fecha        DATETIME2(0)  NOT NULL,
    Monto        DECIMAL(10,2) NOT NULL,
    INDEX CIX_Movimiento_Fecha CLUSTERED (Fecha)
);

CREATE TABLE academia.Cuota (
    CuotaId INT NOT NULL CONSTRAINT PK_Cuota PRIMARY KEY,
    Monto   DECIMAL(10,2) NOT NULL
);

SELECT
    OBJECT_NAME(object_id) AS Tabla,
    name                   AS Indice,
    type_desc              AS Tipo,
    is_primary_key         AS EsPk
FROM sys.indexes
WHERE object_id IN (OBJECT_ID('academia.Movimiento'), OBJECT_ID('academia.Cuota'))
ORDER BY Tabla, Indice;
