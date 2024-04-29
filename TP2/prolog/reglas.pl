% Reglas de inferencia
:- style_check(-singleton).

regla(MN, MN, MP).
regla(MN, PN, PP).
regla(MN, Z, MN).
regla(MN, PP, PN).
regla(MN, MP, MN).
regla(PN, MN, MP).
regla(PN, PN, PP).
regla(PN, Z, PN).
regla(PN, PP, PN).
regla(PN, MP, MN).
regla(Z, MN, PP).
regla(Z, PN, MP).
regla(Z, Z, Z).
regla(Z, PP, PN).
regla(Z, MP, MP).
regla(PP, MN, PN).
regla(PP, PN, PP).
regla(PP, Z, PP).
regla(PP, PP, PP).
regla(PP, MP, MP).
regla(MP, MN, MP).
regla(MP, PN, MP).
regla(MP, Z, PN).
regla(MP, PP, MP).
regla(MP, MP, MP).
