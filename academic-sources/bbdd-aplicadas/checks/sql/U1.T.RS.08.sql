-- u1 · repaso: ISNULL, COALESCE y NULLIF.
DECLARE @Valor CHAR(3) = NULL;
DECLARE @Total INT = 10, @Cantidad INT = 0;

SELECT
    ISNULL(@Valor, 'valor por defecto')                        AS ConIsnull,
    COALESCE(@Valor, 'valor por defecto')                      AS ConCoalesce,
    COALESCE(NULL, NULL, 'tercero')                            AS PrimerNoNulo,
    @Total / NULLIF(@Cantidad, 0)                              AS DivisionSegura,
    ISNULL(@Total / NULLIF(@Cantidad, 0), -1)                  AS DivisionConDefecto;
