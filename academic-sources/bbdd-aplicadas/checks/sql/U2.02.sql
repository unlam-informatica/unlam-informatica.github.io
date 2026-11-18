SELECT CASE WHEN N'Ñandú' COLLATE Latin1_General_CI_AI = N'nandu' THEN 'iguales' ELSE 'distintas' END AS CI_AI_nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_CI_AS = N'nandu' THEN 'iguales' ELSE 'distintas' END AS CI_AS_nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_CS_AI = N'nandu' THEN 'iguales' ELSE 'distintas' END AS CS_AI_nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_CS_AI = N'Nandu' THEN 'iguales' ELSE 'distintas' END AS CS_AI_Nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_100_BIN2 = N'Nandu' THEN 'iguales' ELSE 'distintas' END AS BIN2_Nandu;
