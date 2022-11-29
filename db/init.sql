create table if not exists perfil (
  id serial PRIMARY KEY,
  trabajo VARCHAR(150),
  empresa VARCHAR(150),
  ssn VARCHAR(150),
  residencia VARCHAR(150),
  direccion jsonb,
  grupo_sanguineo VARCHAR(150)
);

INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Academic librarian',
    'Atkinson and Sons',
    '502-08-2407',
    '18978 Kim Lock Apt. 249nNorth Denisebury, OR 27889',
    'A-'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Manufacturing systems engineer',
    'Williams-Peterson',
    '290-81-2837',
    'USS DavisnFPO AA 17145',
    'O+'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Production assistant, radio',
    'Jones, Sanchez and Miller',
    '425-25-9016',
    '60457 Williams ShorenSouth James, IA 99407',
    'O+'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Systems analyst',
    'Smith, Santana and Larson',
    '483-94-8909',
    'Unit 2200 Box 4452nDPO AP 02121',
    'O+'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Systems developer',
    'Hunt, Robbins and Washington',
    '137-95-2348',
    '3944 Crystal Divide Apt. 654nLake Mistyhaven, ME 01756',
    'AB+'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Agricultural consultant',
    'Brown Group',
    '004-99-2045',
    '9888 Meyer GreensnNew Barbarafort, OR 07774',
    'B-'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Air broker',
    'Hernandez, Munoz and Juarez',
    '427-82-2489',
    '2750 Claudia Heights Suite 433nMarkshire, CT 05701',
    'B+'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Civil engineer, contracting',
    'Barrett-Fischer',
    '100-14-4790',
    '4455 Mckee Road Apt. 441nMichaelland, NE 28690',
    'B-'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Designer, multimedia',
    'Richards-Rodriguez',
    '294-37-9820',
    '957 Newman Roads Apt. 359nPort Erikashire, CO 33584',
    'B-'
);
INSERT INTO perfil(
    trabajo,
    empresa,
    ssn,
    residencia,
    grupo_sanguineo
)
VALUES(
    'Development worker, international aid',
    'Edwards, Harvey and Padilla',
    '895-75-4189',
    '021 Hopkins SpringsnNorth Taylorton, IN 12562',
    'A+'
);