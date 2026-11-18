SELECT JSON_OBJECT('codigo': 'P001', 'precio': 1250.50, 'stock': NULL)                AS ObjetoPorDefecto,
       JSON_OBJECT('codigo': 'P001', 'precio': 1250.50, 'stock': NULL ABSENT ON NULL) AS ObjetoSinNulos,
       JSON_ARRAY('azul', 'rojo', NULL)                                                AS ArregloPorDefecto,
       JSON_ARRAY('azul', 'rojo', NULL NULL ON NULL)                                   AS ArregloConNulos,
       JSON_OBJECT('lineas': JSON_ARRAY(1, 2, 3))                                      AS Anidado;
